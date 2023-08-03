from odoo import models, fields


class DigestDigest(models.Model):

    _inherit = 'digest.digest'

     # Fields declaration
    offene_aufgaben = fields.Boolean()
