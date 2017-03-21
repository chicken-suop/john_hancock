# -*- coding: utf-8 -*-
# Copyright (c) 2015, ratskin and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Contract(Document):

	def validate(self):
		if not self.recipient_email:
			frappe.throw("Were you planing on using carrier pigeon to deliver this?\nIf not, then please provide an email.")