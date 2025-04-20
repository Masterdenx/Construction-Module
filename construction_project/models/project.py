from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ConstructionProject(models.Model):
    _name = 'construction.project'
    _description = 'Construction Project'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Nombre del Proyecto', required=True)
    start_date = fields.Date(string='Fecha de Inicio', required=True)
    end_date = fields.Date(string='Fecha de Fin', required=True)
    budget = fields.Float(string='Presupuesto')
    partner_id = fields.Many2one('res.partner', string='Cliente')
    task_ids = fields.One2many('construction.task', 'project_id', string='Tareas')
    progress = fields.Float(string='Progreso (%)', compute='_compute_progress', store=True)

    @api.depends('task_ids.state')
    def _compute_progress(self):
        for project in self:
            tasks = project.task_ids
            if tasks:
                completed = tasks.filtered(lambda t: t.state == 'done')
                project.progress = (len(completed) / len(tasks)) * 100
            else:
                project.progress = 0

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.end_date and record.end_date < record.start_date:
                raise ValidationError("La fecha de fin no puede ser anterior a la fecha de inicio.")

    @api.onchange('progress')
    def _onchange_progress(self):
        for record in self:
            if 49 < record.progress < 51:
                self.env['account.move'].create({
                    'move_type': 'out_invoice',
                    'partner_id': record.partner_id.id,
                    'invoice_line_ids': [(0, 0, {
                        'name': f'Pago parcial del proyecto: {record.name}',
                        'quantity': 1,
                        'price_unit': record.budget * 0.5,
                    })]
                })
