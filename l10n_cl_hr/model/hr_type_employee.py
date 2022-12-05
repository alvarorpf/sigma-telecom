from odoo import api, fields, models, tools, _


class hr_type_employee(models.Model):
    _name = 'hr.type.employee'
    _description = 'Tipo de Empleado'
    
    id_type = fields.Char('Código', required=True)
    name = fields.Char('Nombre', required=True)
    company_id = fields.Many2one('res.company', string='Company', required=True,
                                 default=lambda self: self.env.company)
