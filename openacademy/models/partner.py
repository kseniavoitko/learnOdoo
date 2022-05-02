from odoo import api, fields, models

class PartnerModel(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(string='Instructor')
    session_ids = fields.Many2many('academy.session')
    teacher = fields.Selection([('teacher_level1', "Teacher / Level 1"), ('teacher_level2', "Teacher / Level 2")])