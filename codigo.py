# -*- coding: utf-8 -*-
#from odoo import models, api, fields
import logging

from openerp import api, fields, models, _ 
from openerp.exceptions import UserError, ValidationError
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT as DF


# Este lo usamos para realizar las pruebas
_logger = logging.getLogger(__name__)

class productTemplate(models.Model):
	_inherit = 'res.partner'

	def _default_company(self):
        return self.env['res.company']._company_default_get('res.partner')

	#email = fields.Char()
	#phone = fields.Char()
	fax = fields.Char()