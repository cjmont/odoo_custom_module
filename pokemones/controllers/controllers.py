from odoo import http
from odoo.http import Response
import json


class InvoiceController(http.Controller):

    @http.route('/api/invoices', auth='public', method=['GET', 'POST'], csrf=False)
    def get_invoice(self, **kw):
        try:
            if http.request.httprequest.method == 'POST':              
                partners_create = http.request.env['res.partner'].sudo().create({'name':kw['name']})
                res = json.dumps(partners_create, ensure_ascii=False).encode('utf-8')
                return Response(res, content_type='application/json;charset=utf-8', status=200)

            partners = http.request.env['res.partner'].sudo().search([])           
            ordenes = http.request.env['sale.order.line'].sudo().search([])
            
            partner_list = []

            for partner in partners:
                for sale in ordenes:

                    partner_list.append(
                    {
                            "id": partner.id,
                            "createtime": str(partner.create_date),
                            "document_number": "001-001-00001234", 
                            "customer": {
                                "document_type": "Cédula|RUC|Pasaporte", 
                                "document_number": partner.vat, 
                                "first_name": partner.name,
                                "last_name": "Jaque", 
                                "phone": partner.phone,
                                "address": partner.contact_address, 
                                "email": partner.email
                            },

                            "items": 
                                {
                                "reference": sale.name, 
                                "name": str(sale.display_name),
                                "price": sale.price_reduce,
                                "discount": sale.discount,
                                "subtotal": sale.price_subtotal,
                                "tax": sale.price_tax,
                                "total": sale.price_total
                                }
                        }
                    )
            
            res = json.dumps(partner_list, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)

