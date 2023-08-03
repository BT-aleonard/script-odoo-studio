from odoo import models, fields


class HrEmployee(models.Model):

    _inherit = 'hr.employee'

     # Fields declaration
    besttigungen = fields.Many2many('bestatigungen.mitarb', 'hr_employee_x_bestatigungen_mitarb_rel', string="Bestätigungen")
    YY1rq = fields.Many2one('fleet.vehicle', string="Fahrzeug")
    nationality_2 = fields.Many2one('res.country', string="2. Nationalität (Land)")
    aufenthaltsbewilligung = fields.Selection()
    anrede = fields.Selection()
    personal_raum = fields.Many2one('raume', string="Raum")
    pis_privat_plz = fields.Integer(string="PLZ old")
    kontaktformular = fields.Boolean()
    mitarbeiter_fahrzeug = fields.One2many('fleet.vehicle', 'driver_employee_id', string="Fahrzeug")
    mitarbeiter_assets = fields.One2many('assets', 'asset_mitarbeiter', string="Assets")
    one2many_field_Ze8cw = fields.One2many('fleet.vehicle', 'driver_employee_id', string="New One2many")
    pis_privat_mobile = fields.Char(string="Mobile")
    privat_plz = fields.Char(string="PLZ")
    geschaeftsfahrzeug = fields.Char(string="Geschäftsfahrzeug")
    psi_privat_ort = fields.Char(string="Ort")
    kurzzeichen = fields.Char()
    pis_privat_e_mail = fields.Char(string="E-Mail-Privat")
    direkt_geschftlich = fields.Char(string="Direkt (geschäftlich)")
    pis_strasse = fields.Char(string="Strasse")
    vertragspartner = fields.Many2one('res.company')
