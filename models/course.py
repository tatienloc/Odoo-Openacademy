from odoo import api , fields , models

class Course(models.Model):
    _name = "courses"
    _description = "manage academy"

    name = fields.Char(string="Name" , required = True)
    email = fields.Char(string="Email")
    phone = fields.Integer(string="Phone")
    course = fields.Selection([("python","Python"),("java","Java"),("php","Php")], string="Course" , required=True , default="python")