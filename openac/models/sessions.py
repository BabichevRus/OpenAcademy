# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta

class sessions(models.Model):
    _name = 'openac.sessions'
    _description = 'openac.sessions'

    course = fields.Many2one('openac.course', string='Course', required=True)
    name = fields.Char(string='Name')
    startdate = fields.Date(string='Start Date', default=fields.Date.today())
    enddate   = fields.Date(string='End Date', compute='_compute_enddate')
    duration = fields.Integer(string='Duration')
    hours = fields.Float(string="Duration in hour",
                         compute='_get_hours')
    number_of_seats = fields.Integer(string='Number of seats')
    instructor = fields.Many2one('res.partner', string='Instructor',
                                 domain=['|',('is_instructor', '=', True),
                                     '|',('category_id', '=', 'Учитель/Уровень 2'),
                                     ('category_id', '=', 'Учитель/Уровень 1')
                                        ])

    description = fields.Text(string='Description')
    attendeeslist = fields.Many2many(string='Attendees', comodel_name='res.partner')
    attendeescount = fields.Integer(
        string="Attendees count", compute='_get_attendees_count', store=True)

    percent = fields.Float(string='% filling',compute='_compute_percent_of_taken_seats')
    is_active = fields.Boolean(string='Is active', default=True)
    color = fields.Integer()

    @api.depends('attendeeslist')
    def _get_attendees_count(self):
        for record in self:
            record.attendeescount = len(record.attendeeslist)

    @api.depends('duration')
    def _get_hours(self):
        for record in self:
            record.hours = record.duration * 24

    @api.depends('percent')
    def _compute_percent_of_taken_seats(self):
        for record in self:
            # нужно получить количество участников и вычислить процент относительно числа мест в сессии
            total = len(record.attendeeslist)
            if record.number_of_seats ==0:
                record.percent = 0
            else:
                record.percent = round(total / record.number_of_seats * 100)

    @api.depends('startdate','duration')
    def _compute_enddate(self):
        for record in self:
            record.enddate = record.startdate + timedelta(days=record.duration)

    @api.onchange('number_of_seats', 'attendeeslist')
    def _onchange_percent(self):
        # set auto-changing field
        total = len(self.attendeeslist)

        if total > self.number_of_seats:
            self.percent = round(total / self.number_of_seats * 100)
            return {
                'warning': {
                    'title': "Data entry error",
                    'message': "More participants than places",
                }
            }
        elif self.number_of_seats <=0:
            return {
                'warning': {
                    'title': "Data entry error",
                    'message': "The number of seats must be greater than zero",
                }
            }
        else:
            self.percent = round(total / self.number_of_seats * 100)

    @api.constrains('instructor', 'attendeeslist')
    def _check_instructor_in_attendeeslist(self):
        instructor = self.instructor
        for record in self.attendeeslist:
            if record == instructor:
                raise ValidationError("The instructor is present among the participants")
