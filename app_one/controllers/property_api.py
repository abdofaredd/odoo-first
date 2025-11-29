from odoo import http
from odoo.http import request
import json
from urllib.parse import parse_qs
import math



def valid_response(data,status,pagination_info):
   response_body= {
    'data':data
   }
   if pagination_info:
    response_body['pagination_info']=pagination_info 

   return request.make_json_response(response_body,status=status)  

def invalid_response(error,status):
   response_body= {
    'error':error
   }
   return request.make_json_response(response_body,status=status) 






class propertyApi(http.Controller):

    @http.route("/v1/property",methods=["POST"],type="http",auth="none",csrf=False)

    def post_property(self):
      args =  request.httprequest.data.decode()
      vals = json.loads(args)
    #   res  = request.env['property'].create(vals)

      if not vals.get('name'):
            return request.make_json_response({
                "message": "name is required",
            }, status=400)
      try:
        # res = request.env['property'].sudo().create(vals)
        cr =request.env.cr
        colums=', '.join(vals.keys())
        values=', '.join(['%s']* len(vals))  
        query= f"""INSERT INTO property  ({colums}) VALUES ({values})  RETURNING id , name ,postcode"""
        cr.execute(query,tuple(vals.values()))
        res=cr.fetchone()
        if res:
            return request.make_json_response({
                "message": "property record has been created successfully",
                "id": res[0],
                "name": res[1],
                "postcode": res[2],
            }, status=201)
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

    @http.route("/v1/property/<int:property_id>", methods=['GET'], type='http', auth='none', csrf=False)
    def get_property(self, property_id):
        try:
            property_id = request.env["property"].sudo().search([('id', '=', property_id)], limit=1)
            if not property_id:
                return invalid_response( "ID Does Not Exist", status=404)

            # args = request.httprequest.data.decode()
            # vals = json.loads(args)
            # property_id.write(vals)

            return valid_response({
                "message": "Property updated successfully",
                "id": property_id.id,
                "name": property_id.name,
                "description": property_id.description,
                "postcode": property_id.postcode,
                "expected_price": property_id.expected_price,
            }, status=200)

        except Exception as error:
            return request.make_json_response({
                "message":error

            },status=400)
    

    @http.route("/v1/property/<int:property_id>",methods=['DELETE'],type='http',auth="none",csrf=False)
    def delete_property(self,property_id):
        try:
            property_id = request.env["property"].sudo().search([('id', '=', property_id)])


            if not property_id:
                 return request.make_json_response({
                    "error": "ID Does Not Exist"
                    }, status=404) 
            property_id.unlink()
            return request.make_json_response({
                "message": "Property has been deleted successfully",
                
            }, status=200)




        except Exception as error:
            return request.make_json_response({
                "message":error

            },status=400)
    

    @http.route("/v1/properties", methods=['GET'], type='http', auth='none', csrf=False)
    def get_property_list(self):
        try:
            params= parse_qs(request.httprequest.query_string.decode('utf-8'))
            property_domain=[]

            offset = page = None
            limit = 5 
            if params.get('limit'):
                limit = int(params.get('limit')[0])

            if params.get('page'):
                page = int(params.get('page')[0])


            if page:
                offset=(page * limit) - limit
            if params.get('status'):
                property_domain += [('status' ,'=', params.get('status')[0])]
            property_ids = request.env["property"].sudo().search(property_domain ,offset=offset,limit=limit,order='id Desc')
            property_count = request.env["property"].sudo().search_count(property_domain)

            if not property_ids:
                return invalid_response({ 
                    "error": "there are not records"
                    }, status=404)

            # args = request.httprequest.data.decode()
            # vals = json.loads(args)
            # property_id.write(vals)

            return valid_response([{
                "message": "Property fetched successfully",
                "id": property_id.id,
                "name": property_id.name,
                "description": property_id.description,
                "postcode": property_id.postcode,
                "expected_price": property_id.expected_price,
            } for property_id in property_ids],pagination_info={
                "page": page if page else 1,
                "limit":limit,
                "pages":math.ceil(property_count / limit) if limit else 1,
                "count":property_count,

            }, status=200)

        except Exception as error:
            return request.make_json_response({
                "message":error

            },status=400)
    