from odoo import models, fields


class ProjectTask(models.Model):

    _inherit = 'project.task'

     # Fields declaration
    abteilung = fields.Char(related='project_id.x_studio_many2one_field_JqQAl.name')
    char_field_4XoSV = fields.Char(string="New Text")
    FmJHC = fields.Char(related='project_id.x_studio_many2one_field_j2RB3.display_name', string="New Zugehöriges Feld")
    1FDYL = fields.Boolean(related='project_id.x_studio_eintritt_mirtarbeitende', string="New Zugehöriges Feld")
