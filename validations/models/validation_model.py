# -*- coding: utf-8 -*-
from odoo import models, fields, api


class validationModel(models.Model): 
    _name = 'validations.validation_model'
    _description = 'validation model'


    date = fields.Date("Date", required=True)
    module = fields.Many2one("validations.modules_model", "Module",required=True)
    student = fields.Many2one("validations.students_model", "Student",required=True)
