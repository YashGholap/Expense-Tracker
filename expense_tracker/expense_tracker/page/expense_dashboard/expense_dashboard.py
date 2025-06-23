import frappe

@frappe.whitelist()
def get_total_expense():
    total = frappe.db.sql("""
                          SELECT SUM(amount) as total 
                          FROM `tabExpense`
                          WHERE owner = %s
                          """, frappe.session.user, as_dict= True)
    return total[0] if total and total[0].get("total") else {"total": 0}