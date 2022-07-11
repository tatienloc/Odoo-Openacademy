#from odoo import http


#class Openacademy(http.Controller):
#     @http.route('/openacademy' , auth="public" , type="json" )
#     def index(self,**kw):
#         contacts = http.request.env['courses'].sudo().search([])

#         contact_list = []
#         for contact in contacts:
#             contact_list.append({
#                 'title': contact.title,
#                 'description': contact.description,})
#         return contact_list



# sửa dữ liệu
#         contect = http.request.env["courses"].sudo().search([("id" , "=" , 26)])
#         contect.write({"name" : kw["name"] ,
#                        "email" : kw["email"] ,
#                        "phone" : kw["phone"] ,
#                        "course" : kw["course"]})
#         return kw






# tạo dữ liệu
#         http.request.env['courses'].sudo().create({'name' : kw['name'] , 'email' : kw['email']
#                                                       , 'phone' :kw['phone'] , 'course' :kw['course']})
#         return kw



