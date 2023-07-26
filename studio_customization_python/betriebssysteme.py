from odoo import models, fields


class Betriebssysteme(models.Model):

    _name = 'betriebssysteme'
    _description = 'Betriebssysteme'

     # Fields declaration
    active = fields.Boolean(string="Aktiv")
    name = fields.Char(string="Beschreibung", required=True, translate=True)
    sequence = fields.Integer(string="Reihenfolge")
