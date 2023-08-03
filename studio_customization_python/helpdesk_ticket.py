from odoo import models, fields


class HelpdeskTicket(models.Model):

    _inherit = 'helpdesk.ticket'

     # Fields declaration
    produktfamilie_it_suport = fields.Many2one('produktfamilie.it.su', string="Produktfamilie")
    produktfamilie_kategorie_it_support = fields.Many2one('produktfamilie.kateg', string="Produktfamilie Kategorie")
