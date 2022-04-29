from odoo import models, fields, api

class Teachers(models.Model):
    _name = 'academy.teachers'
    _description = 'academy.teachers'

    name = fields.Char()
    biography = fields.Html()
    course_ids = fields.One2many('academy.courses', 'teacher_id', string="Courses")

class Courses(models.Model):
    _name = 'academy.courses'
    #_inherit = ['mail.thread', 'product.template']
    _inherit = ['product.template']

    name = fields.Char()
    teacher_id = fields.Many2one('academy.teachers', string="Teacher")