import frappe


@frappe.whitelist()
def get_desk_includes():
	"""Return Desk includes exactly as Frappe sees them (for debugging)."""
	return {
		"app_include_css": frappe.get_hooks("app_include_css") or [],
		"app_include_js": frappe.get_hooks("app_include_js") or [],
	}

