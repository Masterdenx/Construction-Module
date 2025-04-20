from odoo import models, fields

class ConstructionTask(models.Model):
    _name = 'construction.task'
    _description = 'Construction Task'

    name = fields.Char(string='Nombre de la Tarea', required=True)
    state = fields.Selection([
        ('pending', 'Pendiente'),
        ('in_progress', 'En Progreso'),
        ('done', 'Completada')
    ], default='pending', string='Estado')
    deadline = fields.Date(string='Fecha Límite')
    user_id = fields.Many2one('res.users', string='Responsable')
    project_id = fields.Many2one('construction.project', string='Proyecto')
