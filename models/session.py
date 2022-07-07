from odoo import  api , fields , models , exceptions

class Session(models.Model):
    _name = "session"
    _descripsion = "Session of course"

    name = fields.Char(string="Name")
    #start_date = fields.Datetime(string="Start Date")
    start_date = fields.Date(default=fields.Date.today , string="Start Date" , readonly=True)
    duration = fields.Integer(string="Duration")
    number_of_seats = fields.Integer(string="Number Of Seats")
    active = fields.Boolean(default = True , string="Active")
    instructor_id = fields.Many2one("res.users" , ondelete = "set null" , string="Instructor" , index= True)
    course_id = fields.Many2one("courses" , ondelete ="cascade" , string="Course" , required = True)
    attendee_ids = fields.Many2many ("res.partner" , string="Attendees")
    taken_seats = fields.Float(string="Taken Seats" , compute ="_taken_seats")

    @api.depends("number_of_seats" , "attendee_ids")
    def _taken_seats(self):
        for r in self:
            if not r.number_of_seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.number_of_seats

    @api.onchange("number_of_seats" , "attendee_ids")
    def _onchange_verify_valid_seats(self):
        if self.number_of_seats < 0 :
            return {
                "warning" : {
                    "title" : "Incorrect 'seats' value",
                    "message" : "the number of availble seats may not be negative",
                }
            }
        elif self.number_of_seats < len(self.attendee_ids):
            return  {
                "warning" : {
                    "title" : "Too many attendees",
                    "message" : "Increase seats or remove excess attendees",
                }
            }

    @api.constrains("instructor_id" ,"attendee_ids" )
    def _check_instructor(self):
        for r in self:
            if r.instructor_id.id in [x.id for x in r.attendee_ids]:
                raise exceptions.ValidationError("A session's instructor can't be an attendees")