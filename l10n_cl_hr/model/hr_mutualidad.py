from odoo import api, fields, models, tools, _


class hr_mutualidad(models.Model):
    _name = 'hr.mutual'
    _description = 'Mutualidad'
    
    codigo = fields.Char('Codigo', required=True)
    name = fields.Char('Nombre', required=True)
    company_id = fields.Many2one('res.company', string='Company', required=True,
                                 default=lambda self: self.env.company)
