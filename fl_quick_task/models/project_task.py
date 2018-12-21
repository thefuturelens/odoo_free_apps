# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ProjectTask(models.Model):
    _inherit = 'project.task'

    date_deadline = fields.Date(string='Deadline', default=lambda self: fields.Date.today())

    @api.multi
    def create_task_dialog(self):
        return {'type': 'ir.actions.act_window_close'}

    @api.multi
    def edit_task_dialog(self):
        form_view = self.env.ref('project.view_task_form2')
        return {
            'name': _('Task'),
            'res_model': 'project.task',
            'res_id': self.id,
            'views': [(form_view.id, 'form'), ],
            'type': 'ir.actions.act_window',
            'target': 'inline'
        }
