from odoo import api , fields , models

class Description(models.Model):
    _name ="description"
    _description = "Course description"

    acourse = fields.Char(string="Courses")
    des = fields.Text(string="Description")