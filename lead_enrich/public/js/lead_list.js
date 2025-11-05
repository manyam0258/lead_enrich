frappe.listview_settings['Lead'] = {
    onload(listview) {
        listview.page.add_actions_menu_item("Apollo Enrich Selected", () => {
            const selected = listview.get_checked_items();
            if (!selected.length) {
                frappe.msgprint("No Leads selected");
                return;
            }

            frappe.call({
                method: "lead_enrich.api.apollo_service.bulk_enrich",
                args: {
                    leads: JSON.stringify(selected.map(r => r.name))
                },
                callback() {
                    frappe.show_alert("Bulk enrichment triggered");
                    listview.refresh();
                }
            });
        });
    }
};
