# -*- coding: utf-8 -*-
from odoo import models, fields, api


class modulesModel(models.Model): 
    _name = 'validations.modules_model'
    _description = 'Modules model'

    name = fields.Char("Modules name", required=True)
    description = fields.Html('Description')
    hours = fields.Char("hourly load (hours)", required=True)
    course = fields.Many2one("validations.course_model", "Course",required=True)
 