
window.frappe = {};
frappe.ready_events = [];
frappe.ready = function(fn) {
	frappe.ready_events.push(fn);
}
window.dev_server = 0;
window.socketio_port = 9000;
window.show_language_picker = false;

frappe.csrf_token='{{csrf_token}}';
frappe.user='{{user}}';


frappe.boot = {{ boot }}
// for backward compatibility of some libs
frappe.sys_defaults = frappe.boot.sysdefaults;





{{path_bundle}}