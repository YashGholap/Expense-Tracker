frappe.pages['expense-dashboard'].on_page_load = function(wrapper) {
    // 1. Create the page layout
    const page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Expense Dashboard',
        single_column: true
    });

    // 2. Empty the layout section to avoid stacking on reload
    const content = $(wrapper).find('.layout-main-section').empty();

    // 3. Append dashboard content
    $(`<div id="dashboard-content">
        <h2>Total Spent: ₹<span id="total-amount">Loading…</span></h2>
        <div id="chart-area"></div>
    </div>`).appendTo(content);

    // 4. Call backend to fetch total expense
    frappe.call({
        method: "expense_tracker.expense_tracker.page.expense_dashboard.expense_dashboard.get_total_expense",
        callback: function(r) {
            console.log("✔️ Backend response:", r.message);
            $("#total-amount").text(r.message.total || 0);
        },
        error: function(err) {
            console.error("❌ Backend error:", err);
        }
    });
};
