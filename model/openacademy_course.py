from openerp import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'

    nano = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
