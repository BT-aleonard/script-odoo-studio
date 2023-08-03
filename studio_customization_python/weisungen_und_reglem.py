from odoo import models, fields


class WeisungenUndReglem(models.Model):

    _name = 'weisungen.und.reglem'
    _description = 'Weisungen und Reglemente'

     # Fields declaration
    name = fields.Char(string="Beschreibung", required=True, translate=True)
