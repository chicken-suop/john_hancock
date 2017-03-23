// Copyright (c) 2016, ratskin and contributors
// For license information, please see license.txt


frappe.ui.form.on("Contract", "request_signature", function(frm) {
	alert("Ordered the tuna\n"+
"Minutes later, still waiting\n"+
"Request is processing\n")
	frappe.call({
		"method": "erpnext_plus_signaturit.send.send",
		"args": {
			"html": frm.doc.contract,
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
		for (var i = 0; i < frm.doc.contract_terms.length; i++) {
			frm.doc.contract = frm.doc.contract.replace((new RegExp("\\["+frm.doc.contract_terms[i]["signature_term"]+"\\]", "g")), frm.doc.contract_terms[i]["value"]);
		}
		frappe.model.set_value(frm.doctype, frm.docname, "contract", frm.doc.contract);
	}
});



// OLD
// --------------------------------------------------

// frappe.ui.form.on("Contract", "request_signature", function(frm) {
// 	console.log("This will take a moment...")

// 	var formData = new FormData();
// 	formData.append("html", frm.doc.contract);
// 	var blob = new Blob([], {type: "text/xml"});
// 	formData.append("blob", blob);

// 	var xhr = new XMLHttpRequest();
// 	xhr.open("POST", "/api/method/erpnext_plus_signaturit.send.to_pdf");
// 	xhr.setRequestHeader("X-Frappe-CSRF-Token", frappe.csrf_token);
// 	xhr.responseType = "arraybuffer";

// 	xhr.onload = function(success) {
// 		if (this.status === 200) {

// 			// var blob = new Blob([success.currentTarget.response], {type: "application/pdf"});
// 			// window.open(URL.createObjectURL(blob));


// 			// The decode() method takes a DataView as a parameter, which is a wrapper on top of the ArrayBuffer.
// 			var dataView = new DataView(success.currentTarget.response);
// 			// The TextDecoder interface is documented at 
// 			var decoder = new TextDecoder("UTF-8");
// 			var decodedString = decoder.decode(dataView);

// 			frappe.call({
// 				"method": "erpnext_plus_signaturit.send.send",
// 				"args": {
// 					"bytes_data": decodedString,
// 					"recipient": frm.doc.recipient_email, 
// 					"recipient_name": frm.doc.recipient_name, 
// 					"subject": frm.doc.subject, 
// 					"body": frm.doc.body
// 				}, callback: function(r) {}
// 			})

// 			console.log(decodedString)
// 		} else {
// 			console.error('Error while requesting', this);
// 		}
// 	};
// 	xhr.send(formData);
// });