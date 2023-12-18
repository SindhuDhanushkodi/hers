// Copyright (c) 2023, Sindhu and contributors
// For license information, please see license.txt

frappe.ui.form.on('HERS', {
	onload: function(frm) {
		let doc_name = frm.doc.name
		if (doc_name.startsWith("new-hers")){
			frappe.call({
				method: "hers.hers.doctype.hers.hers.item_code",
				callback: function(r) {
					frm.set_value("item_code",r.message.missing_numbers)
					frm.set_value('frontend_location', r.message.location)
					// frm.set_df_property('item_code', 'read_only', 1)
					frm.fields_dict['brand'].$input.focus();
				}
			})
		}
	}
});
