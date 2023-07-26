from odoo import models, fields


class AssetUnterkategorie(models.Model):

    _name = 'asset.unterkategorie'
    _description = 'Asset-Unterkategorie'

     # Fields declaration
    active = fields.Boolean(string="Aktiv")
    asset_unterkategorie_kategorie = fields.Many2one('asset.kategorie', string="Asset-Kategorie")
    name = fields.Char(string="Bezeichnung", required=True, translate=True)
    sequence = fields.Integer(string="Reihenfolge")
