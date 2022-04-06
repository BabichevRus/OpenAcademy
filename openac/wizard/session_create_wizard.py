# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SessionCreateWizard(models.TransientModel):

    _name = 'openac.session_create_wizard'
    _description = 'openac.session_create_wizard'

    def default_session(self):
        return self.env['openac.sessions'].browse(self._context.get('active_id'))

    sessions = fields.Many2many(string='Sessins', comodel_name='openac.sessions',
                              required=True, default=default_session)

    attendeeslist = fields.Many2many(string='Attendees', comodel_name='res.partner')

    def action_create_session(self):
        for session in self.sessions:
            session.attendeeslist = self.attendeeslist
        return {}
