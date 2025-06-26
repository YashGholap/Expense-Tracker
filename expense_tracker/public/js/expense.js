frappe.ui.form.on('Expense',{
    refresh:function(frm){
        frappe.call({
            method: "expense_tracker.expense_tracker.api.get_monthly_expense_summary.get_monthly_expense_summary",
            callback: function(r){
                frappe.msgprint("Total Expense: " + r.message.total);
            }
        });
    }
});