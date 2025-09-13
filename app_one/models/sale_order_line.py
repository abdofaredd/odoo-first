from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    extera_Info = fields.Char(string="Extra Info")
