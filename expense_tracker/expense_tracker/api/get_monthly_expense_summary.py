import frappe

@frappe.whitelist()
def get_monthly_expense_summary():
    expenses = frappe.get_all("Expense", fields=["amount"])
    return {"total": sum(exp["amount"] for exp in expenses)}

