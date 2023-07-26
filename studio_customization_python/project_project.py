from odoo import models, fields


class ProjectProject(models.Model):

    _inherit = 'project.project'

     # Fields declaration
    JqQAl = fields.Many2one('hr.department', string="Abteilung")
    j2RB3 = fields.Many2one('hr.employee', string="Mitarbeiter")
    eintritt_mirtarbeitende = fields.Boolean()
    eintritt = fields.Boolean()
    projekt_prioritaet = fields.Selection(string="Priorität")
