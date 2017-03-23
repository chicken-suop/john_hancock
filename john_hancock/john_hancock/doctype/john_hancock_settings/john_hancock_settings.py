# -*- coding: utf-8 -*-
# Copyright (c) 2015, ratskin and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from signaturit_sdk.signaturit_client import SignaturitClient

class JohnHancockSettings(Document):

	def validate(self):
		if "error" in SignaturitClient(self.token).count_signatures():
			frappe.throw("Invalid OAuth token.")