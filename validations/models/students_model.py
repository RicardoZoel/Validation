# -*- coding: utf-8 -*-
from odoo import models, fields, api
import random
import string

class students_model(models.Model): 
    _name = 'validations.students_model'
    _description = 'Students Model'

    name = fields.Char("Name", required=True)
    foto = fields.Binary("Foto")
    age = fields.Integer('Age', required=True)
    password=fields.Char("Password", required=True)
    location = fields.Char('Location', required=True)
    province=fields.Char("Province",required=True)
    email = fields.Char('Email', required=True)
    validations=fields.One2many("validations.validation_model","student","Validations list")
    
    def GeneratePasw(self):
        self.ensure_one()
        self.password=self.get_string(random.randint(3,8), random.randint(3,8))

    def get_string(self,letters_count, digits_count):
        letters = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
        digits = ''.join((random.choice(string.digits) for i in range(digits_count)))

        # Convert resultant string to list and shuffle it to mix letters and digits
        sample_list = list(letters + digits)
        random.shuffle(sample_list)
        # convert list to string
        final_string = ''.join(sample_list)
        return final_string

   