from odoo import api , fields , models

class Product_template(models.Model):
    _inherit = "product.template"

    a_course = fields.Many2one("courses" , string="Course" , ondetele="set null")