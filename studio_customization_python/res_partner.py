from odoo import models, fields


class ResPartner(models.Model):

    _inherit = 'res.partner'

     # Fields declaration
    geheime_identitt = fields.Boolean(string="Geheime Identität")
    hat_ffentliche_identitt = fields.Boolean(string="Hat öffentliche Identität")
    ffentliche_identitt = fields.Char(string="Öffentliche Identität")
    kontakt_mobile_privat = fields.Char(string="Mobile Privat")
    kontakt_email_privat = fields.Char(string="Email Privat")
