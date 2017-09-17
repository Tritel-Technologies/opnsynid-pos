# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class PosOrder(models.Model):
    _inherit = "pos.order"

    table_id = fields.Many2one(
        string="Table",
        comodel_name="pos.table",
        )

