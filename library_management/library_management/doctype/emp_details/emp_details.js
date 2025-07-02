// Copyright (c) 2025, Meeran and contributors
// For license information, please see license.txt


//frappe.call 
// frappe.ui.form.on('Emp Details', {
//     refresh(frm) {
//         frm.add_custom_button("Create Record via Server", function () {
//             frappe.call({
//                 method: "library_management.library_management.doctype.emp_details.emp_details.create_emp_record",
//                 callback: function(r) {
//                     if (r.message) {
//                         frappe.msgprint("New record created: " + r.message);
//                         frappe.set_route("form", "Emp Details", r.message);
//                     }
//                 }
//             });
//         });
//     }
// });

// Client Event:
//-------------



frappe.ui.form.on("Emp Details", {
    //When User Enter the Form Show the Message
    // setup: function(frm) {
    //     frappe.msgprint("Setup: Triggered once when form is created for the first time");
    // },


    //Before Load
    // before_load: function(frm) {
    //     frm.set_df_property('salary','hidden',1)
    //     frappe.msgprint("before_load: Triggered before the form is about to load");
    // },

    // //Onload Load
    // onload: function(frm) {
    //     frappe.msgprint("onload: Triggered when the form is loaded and is about to render");
    //     frm.set_df_property('salary','hidden',1)
    // },

    // Referesh Load
    // refresh: function(frm) {
    //     frappe.msgprint("refresh: Triggered when the form is loaded and is about to render");
    //     frm.set_df_property('salary','hidden',1)
    // },

     // onload_post_render
    // onload_post_render: function(frm) {
    //     frappe.msgprint("onload_post_render: Triggered after the form is loaded and rendered");
    //     frm.set_df_property('salary','hidden',1)
    // },
    

     // validate
    // validate: function(frm) {
    //     frappe.msgprint("validate: Triggered before before_save");
    //     frm.set_df_property('salary','hidden',1)
    // },
    
    // before_discard
    // after_discard: function(frm) {
    //     frappe.msgprint("before_discard: Triggered before discard is called");
    //     console.log("before_discard triggered");
    // },
    
})

