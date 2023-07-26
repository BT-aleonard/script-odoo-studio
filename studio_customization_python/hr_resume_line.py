from odoo import models, fields


class HrResumeLine(models.Model):

    _inherit = 'hr.resume.line'

     # Fields declaration
    arbeitspensum = fields.Float()
