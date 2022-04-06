from odoo import models, fields, api

class Teachers(models.Model):
    _name = 'openac.teachers'
    _description = 'openac.teachers'

    name = fields.Char()