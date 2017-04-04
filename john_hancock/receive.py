import frappe

def update_hourly():
    inbox_if("Hourly")

def update_daily():
    inbox_if("Daily")


def update_weekly():
    inbox_if("Weekly")


def inbox_if(freq):
    if frappe.utils.cint(frappe.db.get_value("John Hancock Settings", None, "enable")):
        if freq == frappe.db.get_value("John Hancock Settings", None, "frequency"):
            inbox()

@frappe.whitelist()
def check():
    try:
        inbox()
    except Exception:
        frappe.errprint(frappe.get_traceback())

def inbox():
    from signaturit_sdk.signaturit_client import SignaturitClient
    # Get data from signaturit using special ID:
    response = SignaturitClient(frappe.db.sql("SELECT MIN(token) FROM `tabJohn Hancock Settings`;")[0][0]).get_signatures()
    tabInbox_values = []

    # frappe.errprint(response)

    for pos, data in enumerate(response):
        # If row doesn't exist then add it, else don't:
        if frappe.db.sql("SELECT COUNT(1) FROM tabInbox WHERE name = '{}';".format(data["documents"][0]["id"]))[0][0] == 0:         
            for x in ["id", "status", "email", "created_at", "file"]: # Values we want to look for in signaturit data
                for key in data["documents"][0]:
                    if key == x:
                        if x == "file":
                            tabInbox_values.append(data["documents"][0][key]["name"])
                        else:
                            tabInbox_values.append(data["documents"][0][key])
            # Insert into frappe database for inbox doctype a new row
            frappe.errprint(tabInbox_values)
            frappe.db.sql("INSERT INTO tabInbox (id, name, status, recipients, date, document_title) VALUES ({}, '{}', '{}', '{}', '{}', '{}');".format(pos+1, *tabInbox_values))
            tabInbox_values = []