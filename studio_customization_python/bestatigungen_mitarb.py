from odoo import models, fields


class BestatigungenMitarb(models.Model):

    _name = 'bestatigungen.mitarb'
    _description = 'Bestätigungen Mitarbeitende'

     # Fields declaration
    name = fields.Char(string="Beschreibung", required=True, translate=True)
    many2many_field_MV6EZ = fields.Many2many('bestatigungen.mitarb.tag', 'x_bestatigungen_mitarb_x_bestatigungen_mitarb_tag_rel_1', string="Bestätigungen Mitarbeitende Tags")
    many2many_field_4WLKZ = fields.Many2many('bestatigungen.mitarb.tag', 'x_bestatigungen_mitarb_x_bestatigungen_mitarb_tag_rel', string="Bestätigungen")
    sequence = fields.Integer(string="Reihenfolge")
    tag_ids = fields.Many2many('bestatigungen.mitarb.tag', 'bestatigungen_mitarb_tag_rel', string="Stichwörter")
    user_id = fields.Many2one('res.users', string="Verantwortlich")
