from odoo import models, fields


class ProduktfamilieItSu(models.Model):

    _name = 'produktfamilie.it.su'
    _description = 'Produktfamilie IT-Support'

     # Fields declaration
    active = fields.Boolean(string="Aktiv")
    name = fields.Char(string="Beschreibung", required=True, translate=True)
    one2many_field_8XgKk = fields.One2many('produktfamilie.kateg', 'produktfamilie_it_support', string="New One2many")
    sequence = fields.Integer(string="Reihenfolge")
