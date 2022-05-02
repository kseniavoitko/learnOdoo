from odoo import api, fields, models

class AcademyCourse(models.Model):
    _name = 'academy.course'
    _description = 'Openacademy Course'

    name = fields.Char(string='Name')
    description = fields.Char(string='Description')
    responsible = fields.Many2one('res.users')
    session_line_ids = fields.One2many('academy.session', 'course_id', string='Session')

    _sql_constraints = [
        ('name_description',
         'check(name != description)',
         'The course description and the course title must be different!'),

        ('name_uniq',
         'unique(name)',
         'Name must be unique!')]

    def copy(self, default=None):
        new_name = 'Copy of ' + self.name
        default = dict(default or {}, name=new_name)
        return super(AcademyCourse, self).copy(default)