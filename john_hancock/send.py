import frappe
from frappe.utils.pdf import get_pdf
import pdfkit

# @frappe.whitelist()
# def to_pdf(html):
#   frappe.local.response.filename = "EPS-{0}.pdf".format(frappe.generate_hash())
#   frappe.local.response.filecontent = get_pdf(html)
#   frappe.local.response.type = "download"

@frappe.whitelist()
def to_pdf(html, path="../apps/erpnext_plus_signaturit/erpnext_plus_signaturit/tmp/doc.pdf"):
    pdfkit.from_string(html, path)
    return path

# def save_pdf(bytes_data):
#   file_path = "../apps/erpnext_plus_signaturit/erpnext_plus_signaturit/tmp/doc.pdf"

#   with open(file_path, "wb") as f:
#       f.write(bytes_data.encode('utf-8'))
#   return file_path

@frappe.whitelist()
def send(html, recipient, recipient_name, subject, body):
    from signaturit_sdk.signaturit_client import SignaturitClient

    file_path = [to_pdf(html)]
    recipients =  [{
        "name": recipient_name,
        "email": recipient
    }]
    sign_params = {
        "subject": subject,
        "body": body
    }
    frappe.errprint(SignaturitClient(frappe.db.sql("SELECT MIN(signaturit_oauth_token) FROM `tabERPNext plus Signaturit Settings`;")[0][0]).create_signature(file_path, recipients, sign_params))