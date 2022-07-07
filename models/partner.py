from odoo import  fields , models

class Partner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(string="Instructor" , default = True)
    session_ids = fields.Many2many("session" , string="Attended Sessions" , readonly = True)


