# Copyright (c) 2023, Sindhu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class HERS(Document):
	pass

@frappe.whitelist()
def item_code():
    doc = frappe.get_list("HERS")
    last_doc = frappe.get_last_doc("HERS")
    missing_numbers = []
    
    location = last_doc.get("frontend_location")
    int_list = [int(item.get("name")) for item in doc]
    int_list.sort()
    for i in range(int_list[0], int_list[-1] + 1):
        if i not in int_list:
            missing_numbers.append(i)
    if not missing_numbers:
        missing_numbers = [int_list[-1] + 1]
    return {"missing_numbers" :missing_numbers, "location": location}
