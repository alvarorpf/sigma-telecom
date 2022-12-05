
import math
from odoo import api, fields, models, tools


class HRHolidaysStatus(models.Model):
    _inherit = 'hr.leave.type'
    is_continued = fields.Boolean('Disccount Weekends')
    company_id = fields.Many2one('res.company', string='Company', required=True,
                                 default=lambda self: self.env.company)


class HRHolidays(models.Model):
    _inherit = 'hr.leave'

    def _get_number_of_days(self, date_from, date_to, employee_id):
        #En el caso de las licencias descontamos dias corridos
        if employee_id and self.holiday_status_id.is_continued:
            time_delta = date_to - date_from
            return math.ceil(time_delta.days + float(time_delta.seconds) / 86400)
        else:
            return super(HRHolidays, self)._get_number_of_days(date_from, date_to, employee_id)


    def name_get(self):
        res = []
        for leave in self:
            if self.env.context.get('short_name'):
                if leave.leave_type_request_unit == 'hour':
                    res.append((leave.id, ("%s : %.2f hour(s)") % (leave.name or leave.holiday_status_id.name, leave.number_of_hours_display)))
                else:
                    res.append((leave.id, ("%s : %.2f day(s)") % (leave.name or leave.holiday_status_id.name, leave.number_of_days)))
            else:
                if leave.holiday_type == 'company':
                    target = leave.mode_company_id.name
                elif leave.holiday_type == 'department':
                    target = leave.department_id.name
                elif leave.holiday_type == 'category':
                    target = leave.category_id.name
                else:
                    target = leave.employee_id.name
                if leave.leave_type_request_unit == 'hour':
                    res.append(
                        (leave.id,
                        _("%s on %s : %.2f hour(s)") %
                        (target, leave.holiday_status_id.name, leave.number_of_hours_display))
                    )
                else:
                    res.append(
                        (leave.id,
                        ("%s on %s : %.2f day(s)") %
                        (target, leave.holiday_status_id.name, leave.number_of_days))
                    )
        return res