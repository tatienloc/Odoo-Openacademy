from odoo import api , fields , models

class Course(models.Model):
    _name = "courses"
    _description = "manage academy"

    title = fields.Char(string="Title" , required = True)
    description = fields.Text(string="Description")

    responsible_id = fields.Many2one("res.users" , ondelete = "set null" , string="Responsible" , index= True)
    session_ids = fields.One2many("session" , "course_id" , string="Sessions")


class Course2(models.Model):
    _inherit = "courses"

    product_ids = fields.One2many("product.template", "a_course")
    product_ids_count = fields.Integer(string="Product Count" , compute="_product_ids_count")

    @api.depends("product_ids")
    def _product_ids_count(self):
        for r in self:
            r.product_ids_count = len(r.product_ids)


    _sql_constraints = [
        ("title_description_check",
         "CHECK(title != description)",
         "the title of the course should not be the description"),
    ]