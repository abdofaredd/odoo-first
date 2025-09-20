from odoo import models,fields



class AccountMove(models.Model):
    _inherit='account.move'
    # _name='name'


    def action_do_something(self):
        print(self, 'lorem5')
