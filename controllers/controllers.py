from odoo import http


class Openacademy(http.Controller):
     @http.route('/openacademy' , auth="public" , type="json" )
     def index(self, **kw):
# sửa dữ liệu
         contect = http.request.env["courses"].sudo().search([("id" , "=" , 26)])
         contect.write({"name" : kw["name"] ,
                        "email" : kw["email"] ,
                        "phone" : kw["phone"] ,
                        "course" : kw["course"]})
         return kw






# tạo dữ liệu
#         http.request.env['courses'].sudo().create({'name' : kw['name'] , 'email' : kw['email']
#                                                       , 'phone' :kw['phone'] , 'course' :kw['course']})
#         return kw

# lấy dữ liệu
#         contacts = http.request.env['courses'].sudo().search([])

#         contact_list = []
#        for contact in contacts:
#           contact_list.append(
#          {
#                'name' : contact.name ,
#               'email' : contact.email ,
#              'phone' : contact.phone ,
#             'course' : contact.course ,
#     })
#        return contact_list

