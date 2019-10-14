# -*- coding: utf-8 -*-

from odoo import models, api
from datetime import datetime


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    def send_birthday_wish(self):
        today_date = datetime.today().date()
        for employee in self.env['hr.employee'].search([]):
            if employee.birthday:
                if today_date.day == employee.birthday.day and today_date.month == employee.birthday.month:
                    template_id = self.env.ref('fl_birthday_wish.email_birthday_wishes_employee_template')
                    template_id.send_mail(employee.id, force_send=True)
        for partner in self.env['res.partner'].search([]):
            if partner.birthday:
                if today_date.day == partner.birthday.day and today_date.month == partner.birthday.month:
                    template_id = self.env.ref('fl_birthday_wish.email_birthday_wishes_partner_template')
                    template_id.send_mail(partner.id, force_send=True)
