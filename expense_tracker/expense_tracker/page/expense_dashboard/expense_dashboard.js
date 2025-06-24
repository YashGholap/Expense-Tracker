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

    frappe.call({
        method: "expense_tracker.expense_tracker.page.expense_dashboard.expense_dashboard.get_expense_by_category",
        callback: function(r) {
            if(r.message && r.message.length){
                const labels = r.message.map(row => row.category);
                const values = r.message.map(row => row.total);

                new frappe.Chart("#chart-area",{
                    title: "Expenses by Category",
                    data : {
                        labels: labels,
                        datasets: [{ values: values }]
                    },
                    type: 'pie',
                    height: 350
                });
            }else{
                $('#chart-area').html("<p>No expenses found.</p>");
            }
        },
        error: function(err){
            console.error("Chart load failed: ", err);
            $("#chart-area").html("<p> Error Loading Chart.</p>")
        }
    });

    page.add_inner_button("Manage All Expenses", () => {
    frappe.set_route("List", "Expense");
    });
};
