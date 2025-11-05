frappe.ui.form.on("Lead", {
    refresh(frm) {

        frm.add_custom_button("Apollo Enrich", () => {

            frappe.call({
                method: "lead_enrich.api.apollo_service.enrich_single_lead",
                args: { lead_name: frm.doc.name },

                callback(r) {
                    frm.reload_doc();
                    frappe.show_alert({
                        message: __("Apollo Enrichment Completed"),
                        indicator: "green"
                    });
                    return false;
                },

                error(r) {
                    frappe.show_alert({
                        message: __("Apollo Enrichment Failed"),
                        indicator: "red"
                    });
                }
            });

        });

    }
});
