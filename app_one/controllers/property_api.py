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