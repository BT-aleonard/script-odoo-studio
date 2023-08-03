from odoo import models, fields


class AssetsTag(models.Model):

    _name = 'assets.tag'
    _description = 'Assets Tags'

     # Fields declaration
    color = fields.Integer(string="Farbe")
    name = fields.Char(required=True)
