from odoo import models, fields

class Contract(models.Model):
    _name = 'contract.contract'
    _description = 'Contract'

    name = fields.Char(string='Contract Name', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    amount = fields.Float(string='Contract Amount', required=True)
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)