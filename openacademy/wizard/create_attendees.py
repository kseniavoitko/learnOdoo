from odoo import api, fields, models

class CreateAttendeesWizard(models.Model):
    _name = 'create.attendees.wizard'
    _description = 'Create Attendees Wizard'

    def default_session(self):
        return self.env['academy.session'].browse(self._context.get('active_id'))

    session_id = fields.Many2many('academy.session', string='Session', required=True, default=default_session)
    attendee_ids = fields.Many2many('res.partner', string='Attendees')

    def action_create_attendees(self):
        for record in self.session_id:
            record.attendee_ids = self.attendee_ids