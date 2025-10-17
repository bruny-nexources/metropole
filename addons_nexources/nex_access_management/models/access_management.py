# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccessManagement(models.Model):
    _inherit = "access.management"

    role_ids = fields.Many2many(comodel_name="res.users.role", string="Roles")
    user_ids = fields.Many2many(
        "res.users",
        "access_management_users_rel_ah",
        "access_management_id",
        "user_id",
        "Users",
        compute="_compute_user_ids",
        store=True,
    )

    @api.depends("role_ids", "role_ids.user_ids")
    def _compute_user_ids(self):
        for access in self:
            authorized_users = list(
                set(
                    user_id for role in access.role_ids for user_id in role.user_ids.ids
                )
            )
            access.user_ids = [(6, 0, authorized_users)]
