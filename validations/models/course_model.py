# -*- coding: utf-8 -*-
from odoo import models, fields, api


class courseModel(models.Model): 
    _name = 'validations.course_model'
    _description = 'course model'

    name = fields.Char("Category name", required=True)
    description = fields.Html('Description')
    modules=fields.One2many("validations.modules_model","course","Modules list")
