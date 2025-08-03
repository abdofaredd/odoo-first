from odoo import models,fields



class Owner(models.Model):
    _name='owner'

    name=fields.Char(required=True)
    phone=fields.Char()
    address=fields.Char()


    property_ids=fields.One2many('property','owner_id')
    # email=fields.Char(required=True)
    # city=fields.Char(required=True)
    # state=fields.Char(required=True)
    # zip=fields.Char(required=True)
    # country=fields.Char(required=True)
    # property_ids=fields.One2many('property','owner_id')