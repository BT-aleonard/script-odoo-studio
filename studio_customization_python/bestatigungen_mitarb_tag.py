from odoo import models, fields


class BestatigungenMitarbTag(models.Model):

    _name = 'bestatigungen.mitarb.tag'
    _description = 'Bestätigungen Mitarbeitende Tags'

     # Fields declaration
    color = fields.Integer(string="Farbe")
    name = fields.Char(required=True)
