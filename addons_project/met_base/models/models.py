# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class met_base(models.Model):
#     _name = 'met_base.met_base'
#     _description = 'met_base.met_base'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

