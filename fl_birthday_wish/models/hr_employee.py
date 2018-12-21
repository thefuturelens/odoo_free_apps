# -*- coding: utf-8 -*-

from odoo import models, api
from datetime import datetime


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    @api.multi
    def send_birthday_wish(self):
        today_date = datetime.today().date()
        for employee in self.env['hr.employee'].search([]):
            if employee.birthday:
                emp_birthdate = datetime.strptime(employee.birthday, '%Y-%m-%d').date()
                if today_date.day == emp_birthdate.day and today_date.month == emp_birthdate.month:
                    template_id = self.env.ref('fl_birthday_wish.email_birthday_wishes_employee_template')
                    template_id.send_mail(employee.id, force_send=True)
        for partner in self.env['res.partner'].search([]):
            if partner.birthday:
                cust_birthdate = datetime.strptime(partner.birthday, '%Y-%m-%d').date()
                if today_date.day == cust_birthdate.day and today_date.month == cust_birthdate.month:
                    template_id = self.env.ref('fl_birthday_wish.email_birthday_wishes_partner_template')
                    template_id.send_mail(partner.id, force_send=True)
