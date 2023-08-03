from odoo import models, fields


class WeisungenUndReglemTag(models.Model):

    _name = 'weisungen.und.reglem.tag'
    _description = 'Weisungen und Reglemente Tags'

     # Fields declaration
    color = fields.Integer(string="Farbe")
    name = fields.Char(required=True)
