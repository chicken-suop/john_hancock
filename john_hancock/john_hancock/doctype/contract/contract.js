// Copyright (c) 2016, ratskin and contributors
// For license information, please see license.txt


frappe.ui.form.on("Contract", "request_signature", function(frm) {
	alert("Ordered the tuna\n"+
"Minutes later, still waiting\n"+
"Request is processing\n")
	frm.call({
		"method": "john_hancock.send.send",
		"args": {
			"html": frm.doc.text,
			"recipient": frm.doc.recipient_email, 
			"recipient_name": frm.doc.recipient_name, 
			"subject": frm.doc.subject, 
			"body": frm.doc.body
		}, callback: function(r) {}
	})
});

frappe.ui.form.on("Contract", "edit_contract", function(frm) {
	// if terms were provided, continue
	if (typeof frm.doc.contract_terms !== 'undefined' && frm.doc.contract_terms !== null) {
		console.log("Yes")
		for (var i = 0; i < frm.doc.contract_terms.length; i++) {
			frm.doc.contract = frm.doc.contract.replace((new RegExp("\\{"+frm.doc.contract_terms[i]["signature_term"]+"\\}|"+"\\["+frm.doc.contract_terms[i]["signature_term"]+"\\]", "g")), frm.doc.contract_terms[i]["value"]);
		}
		console.log([frm.doctype, frm.docname, "text", frm.doc.contract])
		// frappe.model.set_value(frm.doctype, frm.docname, "contract", frm.doc.contract);
		frappe.model.set_value(frm.doctype, frm.docname, "text", frm.doc.contract);
		// $(frm.fields_dict.contract.wrapper).html(frm.doc.contract)
	}
});