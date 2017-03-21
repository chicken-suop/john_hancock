// Copyright (c) 2016, ratskin and contributors
// For license information, please see license.txt

frappe.ui.form.on("ERPNext plus Signaturit Settings", "affect_em_button", function(frm) {
    
    frappe.call({
        "method": "erpnext_plus_signaturit.receive.check",
        "args": {},
        callback: function(r) {}
    });
});