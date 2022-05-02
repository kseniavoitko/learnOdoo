from datetime import date
from odoo.exceptions import ValidationError
from odoo import api, fields, models

class AcademySession(models.Model):
    _name = 'academy.session'
    _description = 'Openacademy Session'

    name = fields.Char(string='Name')
    start_date = fields.Date(string='Start date', default=date.today())
    end_date = fields.Date(string='End date')
    duration = fields.Integer(string='Duration')
    number_of_seats = fields.Integer(string='Number of seats')
    instructor = fields.Many2one('res.partner', domain=['|', ('instructor', '=', True),
                                                        ('teacher', 'in', ('teacher_level1', 'teacher_level2'))])
    course_id = fields.Many2one('academy.course', required=True, string='Course')
    attendee_ids = fields.Many2many('res.partner', string='Attendees')
    percentage_of_taken_seats = fields.Float(string='Percentage of taken seats', compute='_compute_percentage')
    active = fields.Boolean(string='Active', default=True)
    attendees_count = fields.Integer(compute='_compute_attendees_count', store=True)

    @api.depends('attendee_ids')
    def _compute_attendees_count(self):
        for record in self:
            record.attendees_count = len(record.attendee_ids)

    @api.depends('attendee_ids', 'number_of_seats')
    def _compute_percentage(self):
        for record in self:
            if record.number_of_seats == 0:
                record.percentage_of_taken_seats = 0
            else:
                record.percentage_of_taken_seats = record.attendees_count * 100 / record.number_of_seats

    @api.onchange('number_of_seats')
    def _onchange_number_of_seats(self):
        if self.number_of_seats < 0:
            self.number_of_seats = 0
            return {
                'warning': {
                    'title': "Incorrect value",
                    'message': "Number of seats must be positive",
                }
            }

    @api.onchange('attendee_ids', 'number_of_seats')
    def _onchange_attendee_ids(self):
        if self.number_of_seats < self.attendees_count:
            return {
                'warning': {
                    'title': "Incorrect value",
                    'message': "The number of attendees must be less than the number of seats",
                }
            }

    @api.constrains('attendee_ids', 'instructor')
    def _check_attendee_ids(self):
        for record in self:
            if record.instructor in record.attendee_ids:
                raise ValidationError("The instructor must not be present in the attendees of his/her own session")