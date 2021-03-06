# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    pos_tax_ids = fields.Many2many(
        string="POS Taxes",
        comodel_name="account.tax",
        relation="product_template_pos_taxes_rel",
        column1="product_id",
        column2="tax_id"
    )
