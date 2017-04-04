// Copyright (c) 2016, ratskin and contributors
// For license information, please see license.txt

frappe.ui.form.on("Inbox", "onload", function(frm) {
	console.log("step 1: done")
	frappe.call({
		"method": "john_hancock.receive.check",
		"args": {},
		callback: function(r) {}
	});
	console.log("step 2: done")
});