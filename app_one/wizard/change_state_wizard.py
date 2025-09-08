from odoo import fields , models


class changeState(models.TransientModel):
    _name = 'change.state'
    _description = 'changeStateWizard'


    property_id=fields.Many2one('property')
    reason=fields.Char()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending')
    ], default='draft')



    def action_confirm(self):
       if self.property_id.status == 'closed':
            self.property_id.status =self.state
            self.property_id.property_history_record('closed',self.state,self.reason)
        # action=self.env['ir.actions.actions'].for_xml_id('app_one.change_state_wizard_action')
        # action['context']={
        #     'default_property_id':self.id}
        # return action
    
