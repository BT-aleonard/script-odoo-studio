from odoo import models, fields


class VmHostserver(models.Model):

    _name = 'vm.hostserver'
    _description = 'VM-Hostserver'

     # Fields declaration
    active = fields.Boolean(string="Aktiv")
    name = fields.Char(string="Beschreibung", required=True, translate=True)
    sequence = fields.Integer(string="Reihenfolge")
