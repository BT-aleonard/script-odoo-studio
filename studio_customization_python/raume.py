from odoo import models, fields


class Raume(models.Model):

    _name = 'raume'
    _description = 'Räume'

     # Fields declaration
    active = fields.Boolean(string="Aktiv")
    name = fields.Char(string="Beschreibung", required=True, translate=True)
    sequence = fields.Integer(string="Reihenfolge")
