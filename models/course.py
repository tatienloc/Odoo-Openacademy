from odoo import api , fields , models

class Course(models.Model):
    _name = "courses"
    _description = "manage academy"

    title = fields.Char(string="Title" , required = True)
    description = fields.Text(string="Description")

    responsible_id = fields.Many2one("res.users" , ondelete = "set null" , string="Responsible" , index= True)
    session_ids = fields.One2many("session" , "course_id" , string="Sessions")