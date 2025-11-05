frappe.ui.form.on('Lead', {
    refresh(frm) {
        if (!frm.is_new()) {
            frm.add_custom_button("Enrich via Apollo", () => {
                frappe.call({
                    method: "lead_enrich.api.apollo_service.enrich_single_lead",
                    args: { lead_name: frm.doc.name },
                    callback(r) {
                        frappe.show_alert(r.message);
                        frm.reload_doc();
                    }
                });
            }, __("Actions"));
        }
    }
});
