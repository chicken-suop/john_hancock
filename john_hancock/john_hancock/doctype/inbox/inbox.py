# -*- coding: utf-8 -*-
# Copyright (c) 2015, ratskin and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Inbox(Document):
	pass
	# def validate(self):
	# 	from signaturit_sdk.signaturit_client import SignaturitClient

	# 	conn = SignaturitClient(self.token)
	# 	try:
	# 		conn.create_signature("", "", "")
	# 	except:
	# 		frappe.throw("Your OAuth Token isn't correct.")