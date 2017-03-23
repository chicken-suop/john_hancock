// Copyright (c) 2016, ratskin and contributors
// For license information, please see license.txt

frappe.ui.form.on("John Hancock Settings", "affect_em_button", function(frm) {
    
    frappe.call({
        "method": "john_hancock.receive.check",
        "args": {},
        callback: function(r) {}
    });
});