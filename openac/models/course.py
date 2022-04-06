# -*- coding: utf-8 -*-

from odoo import models, fields, api

class course(models.Model):
    _name = 'openac.course'
    _description = 'openac.course'

    name = fields.Char(string='Name')
    responsible = fields.Many2one('res.users', string='Responsible', required=False)
    description = fields.Text(string='Description')
    sessionslist = fields.One2many(string="Sessions", comodel_name='openac.sessions', inverse_name='course')

    _sql_constraints = [('name_uniq',
                         'UNIQUE (name)',
                         'Course all already exists'),]

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        default = dict(default or {})
        if 'name' not in default:
            default['name'] = self.name + " (Copy)"
        return super(course, self).copy(default)

