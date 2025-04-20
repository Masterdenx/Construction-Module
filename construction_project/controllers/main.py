# controllers/main.py

from odoo import http
from odoo.http import request
from odoo.tools.translate import _

class ConstructionAPI(http.Controller):

    @http.route('/api/project/status/<int:project_id>', type='json', auth='public', methods=['POST'], csrf=False)
    def get_project_status(self, project_id):
        project = request.env['construction.project'].sudo().browse(project_id)

        if not project.exists():
            return {
                'error': True,
                'message': _('Proyecto no encontrado')
            }

        if project.progress == 0:
            estado = "No iniciado"
        elif project.progress == 100:
            estado = "Completado"
        else:
            estado = "En progreso"

        return {
            'id': project.id,
            'nombre': project.name,
            'avance': project.progress,
            'estado': estado
        }
