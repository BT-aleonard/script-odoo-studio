from odoo import models, fields


class DocumentsDocument(models.Model):

    _inherit = 'documents.document'

     # Fields declaration
    dok_dokumentdatum = fields.Date(string="Dokumentdatum")
