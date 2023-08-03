from odoo import models, fields


class ProduktfamilieKateg(models.Model):

    _name = 'produktfamilie.kateg'
    _description = 'Produktfamilie Kategorie IT-Support'

     # Fields declaration
    active = fields.Boolean(string="Aktiv")
    name = fields.Char(string="Beschreibung", required=True, translate=True)
    produktfamilie_it_support = fields.Many2one('produktfamilie.it.su', string="Produktfamilie IT-Support")
    sequence = fields.Integer(string="Reihenfolge")
