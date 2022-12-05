from odoo import api, fields, models, tools, _


class hr_isapre(models.Model):
    _name = 'hr.isapre'
    _description = 'Isapres'
    
    codigo = fields.Char('Codigo', required=True)
    name = fields.Char('Nombre', required=True)
    rut = fields.Char('RUT', required=True)
    company_id = fields.Many2one('res.company', string='Company', required=True,
                                 default=lambda self: self.env.company)

