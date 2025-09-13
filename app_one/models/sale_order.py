from odoo import models,fields

class SaleOrder(models.Model):
    _inherit='sale.order'

    property_id=fields.Many2one('property')
    def acion_confirm(self):
        res=super(SaleOrder,self).acion_confirm()
        print("sale order confirmed")
        return res
