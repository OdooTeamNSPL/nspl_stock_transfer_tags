from odoo import models, fields

class StockPickingTag(models.Model):
    _name = 'stock.picking.tag'
    _description = 'Stock Transfer Tag'
    _order = 'name'

    name = fields.Char("Name", required=True, translate=True)

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    tag_ids = fields.Many2many('stock.picking.tag', string="Tags")