# -*- coding: utf-8 -*-

from odoo import models, fields

class partner(models.Model):
    _inherit = 'res.partner'
    _description = 'res.partner'
    is_instructor = fields.Boolean(string='Instructor')
    sessionslist = fields.Many2many(string="Sessions", comodel_name='openac.sessions')



