from odoo import http
from odoo.http import request
import json



class propertyApi(http.Controller):

    @http.route("/v1/property",methods=["POST"],type="http",auth="none",csrf=False)

    
    def post_property(self):
    #    args =  request.httprequest.data.decode()
    #    vals = json.loads(args)
    #    res  = request.env['property'].create(vals)


      args = request.httprequest.data.decode()
      vals = json.loads(args)

      if not vals.get('name'):
            return request.make_json_response({
                            "message": "name is required",
                            
                        }, status=400)


      try:
        res = request.env['property'].sudo().create(vals)
        if res:
            return request.make_json_response({
                "message": "property record has been created successfully",
                "id": res.id,
                "name": res.name
            }, status=201)
        # else:
        #     return request.make_json_response({
        #         "message": "Failed to create property"
        #     }, status=400)
      except Exception as error:
        return request.make_json_response({
            "message":error

        },status=400)
    
    @http.route("/v1/property/json", methods=['POST'],type='json',auth='none',csrf=False)

    def post_property_json(self):

      args = request.httprequest.data.decode()
      vals = json.loads(args)
      res  = request.env['property'].sudo().create(vals)
      if res :
        return[
            {
                "message":"property has been created"
            }
        ]


    @http.route("/v1/property/<int:property_id>", methods=['PUT'], type='http', auth='none', csrf=False)
    def update_property(self, property_id):
        try:
            property_id = request.env["property"].sudo().search([('id', '=', property_id)], limit=1)
            if not property_id:
                return request.make_json_response({"error": "ID Does Not Exist"}, status=404)

            args = request.httprequest.data.decode()
            vals = json.loads(args)
            property_id.write(vals)

            return request.make_json_response({
                "message": "Property updated successfully",
                "id": property_id.id,
                "name": property_id.name
            }, status=200)

        except Exception as error:
            return request.make_json_response({
                "message":error

            },status=400)