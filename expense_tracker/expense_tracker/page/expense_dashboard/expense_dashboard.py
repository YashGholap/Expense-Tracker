import frappe

@frappe.whitelist()
def get_total_expense():
    total = frappe.db.sql("""
                          SELECT SUM(amount) as total 
                          FROM `tabExpense`
                          WHERE owner = %s
                          """, frappe.session.user, as_dict= True)
    return total[0] if total and total[0].get("total") else {"total": 0}

@frappe.whitelist()
def get_expense_by_category():
    result = frappe.db.sql("""
                          SELECT category, SUM(amount) as total 
                          FROM `tabExpense`
                          WHERE owner = %s
                          GROUP BY category
                          """, frappe.session.user, as_dict= True)
    return result or []

@frappe.whitelist()
def get_recent_expenses():
    recent = frappe.db.sql("""
                           SELECT name, category, amount, description, date
                           FROM `tabExpense`
                           WHERE owner = %s
                           ORDER BY date DESC
                           LIMIT 10
                           """, frappe.session.user, as_dict=True)
    return recent