# Copyright (c) 2025, Meeran and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class EmpDetails(Document):
	pass
	# def before_print(self, print_settings):
	# 	frappe.msgprint("Before print triggered via backend")

	
    # def on_submit(self):
    #     frappe.msgprint(f"After Submitable Document")


    # def before_save(self):
    #     frappe.msgprint("Before Submit Document")


    # def after_delete(self):
    #     frappe.msgprint("After delete")
		
    # def on_trash(self):
    #     frappe.msgprint("Before Delete")

    # def on_cancel(self):
    #     frappe.msgprint("This document is about to be cancelled.")

    # def before_cancel(self):
    #     frappe.msgprint("This document is about to be cancelled.")


    # def on_submit(self):
    #     frappe.msgprint("📤 After Submit fired!")
    # #     frappe.msgprint("The document is about to be submitted!")

	# # Before Save
	# def before_save(self):
	#     if self.first_name and self.last_name:
	#         self.full_name = f"{self.first_name} {self.last_name}"
	#         frappe.msgprint("The Event of Before save worked")

    # After Save
    # def after_save(self):
    #     frappe.msgprint(f"Successfully saved record: {self.full_name}")

    # # Before Insert
    # def before_insert(self):
    #     frappe.msgprint("The Event of Before insert worked")

    # # After Insert
    # def after_insert(self):
    #     frappe.msgprint("After Insert")
	
	# Before Validate
	# def before_validate(self):
	# 	frappe.msgprint("The before_validate event fired")
	
	# After Validate
	# def validate(self):
	# 	frappe.msgprint("Validation completed successfully!")



#Create The Record Using API
#--------------------------

# @frappe.whitelist()
# def create_emp_record():
#     doc = frappe.get_doc({
#         "doctype": "Emp Details",
#         "first_name": "Kumar",
#         "last_name": "RJ",
#         "salary": 12000
#     })
#     doc.insert()
#     return doc.name

    def after_insert(self):
        try:
            frappe.db.sql("""
            SELECT 
            """)


            
