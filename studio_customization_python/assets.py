from odoo import models, fields


class Assets(models.Model):

    _name = 'assets'
    _description = 'Assets'

     # Fields declaration
    active = fields.Boolean(string="Aktiv", tracking=True)
    asset_unterkategorie = fields.Many2one('asset.unterkategorie', string="Kategorie")
    name = fields.Char(string="Beschreibung", required=True, translate=True, tracking=True)
    server_betriebssystem = fields.Many2one('betriebssysteme', string="Betriebssystem")
    image = fields.Binary(string="Bild")
    asset_mitarbeiter = fields.Many2one('hr.employee', string="Verantwortlich")
    server_cluster = fields.Selection(string="Cluster")
    stammkategorie = fields.Char(related='asset_unterkategorie.x_studio_asset_unterkategorie_kategorie.x_name')
    asset_raum_mitarbeiter = fields.Char(related='asset_mitarbeiter.x_studio_personal_raum.display_name', string="Büro")
    asset_anschaffungsdatum = fields.Date(string="Anschaffungsdatum")
    server_anti_virus = fields.Boolean(string="Anti Virus")
    server_bemerkungen = fields.Text(string="Bemerkungen")
    asset_qr_code = fields.Char(string="QR-Code")
    seriennummer = fields.Char()
    server_ip_ilo = fields.Char(string="IP / ILO")
    asset_harddisk = fields.Char(string="Harddisk")
    server_harddisk_gb = fields.Char(string="Harddisk (GB)")
    grafik_auflsung = fields.Char(string="Grafik / Auflösung")
    server_second_ip = fields.Char(string="Second-IP")
    asset_computername = fields.Char(string="Computername")
    server_care_pack = fields.Char(string="Care Pack ")
    mac_adresse = fields.Char(string="MAC-Adresse")
    server_haupt_ip = fields.Char(string="Haupt-IP")
    server_ram_gb = fields.Char(string="RAM (GB)")
    ram_gb = fields.Char(string="RAM (GB)")
    server_modell = fields.Char(string="Modell")
    standort = fields.Many2one('raume')
    sequence = fields.Integer(string="Reihenfolge")
    tag_ids = fields.Many2many('assets.tag', 'assets_tag_rel', string="Stichwörter")
    company_id = fields.Many2one('res.company', string="Unternehmen", tracking=True)
    server_vmhost = fields.Many2one('vm.hostserver', string="VM-Hostserver")
    currency_id = fields.Many2one('res.currency', string="Währung")
    value = fields.Float(string="Kaufpreis", tracking=True)
