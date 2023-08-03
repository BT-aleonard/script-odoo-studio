from odoo import models, fields


class AssetKategorie(models.Model):

    _name = 'asset.kategorie'
    _description = 'Asset-Kategorie'

     # Fields declaration
    active = fields.Boolean(string="Aktiv")
    name = fields.Char(string="Beschreibung", required=True, translate=True)
    asset_kategorie_untergategorie = fields.One2many('asset.unterkategorie', 'asset_unterkategorie_kategorie', string="Untergategorie")
    sequence = fields.Integer(string="Reihenfolge")
