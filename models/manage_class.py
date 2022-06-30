from odoo import api , fields , models

class Manageclass(models.Model):
    _name = "manage_class"
    _description = "manage class"

    a_course = fields.Selection(([("python","Python"),("java","Java"),("php","PhP")]),default="python",string="Course",required=True)
    class_id = fields.Many2one("courses",string="Name",required=True)

