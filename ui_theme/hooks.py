# app_name = "ui_theme"
# app_title = "Ui Theme"
# app_publisher = "Darshana Patil"
# app_description = "Custom UI theme and interface enhancements."
# app_email = "darshanap01@brainmine.ai"
# app_license = "mit"

# # Apps
# # ------------------

# # required_apps = []

# # Each item in the list will be shown as an app in the apps page
# # add_to_apps_screen = [
# # 	{
# # 		"name": "ui_theme",
# # 		"logo": "/assets/ui_theme/logo.png",
# # 		"title": "Ui Theme",
# # 		"route": "/ui_theme",
# # 		"has_permission": "ui_theme.api.permission.has_app_permission"
# # 	}
# # ]

# # Includes in <head>
# # ------------------

# # include js, css files in header of desk.html
# # app_include_css = "/assets/ui_theme/css/ui_theme.css"
# # app_include_js = "/assets/ui_theme/js/ui_theme.js"

# # include js, css files in header of web template
# # web_include_css = "/assets/ui_theme/css/ui_theme.css"
# # web_include_js = "/assets/ui_theme/js/ui_theme.js"

# # include custom scss in every website theme (without file extension ".scss")
# # website_theme_scss = "ui_theme/public/scss/website"

# # include js, css files in header of web form
# # webform_include_js = {"doctype": "public/js/doctype.js"}
# # webform_include_css = {"doctype": "public/css/doctype.css"}

# # include js in page
# # page_js = {"page" : "public/js/file.js"}

# # include js in doctype views
# # doctype_js = {"doctype" : "public/js/doctype.js"}
# # doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# # doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# # doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# # Svg Icons
# # ------------------
# # include app icons in desk
# # app_include_icons = "ui_theme/public/icons.svg"

# # Home Pages
# # ----------

# # application home page (will override Website Settings)
# # home_page = "login"

# # website user home page (by Role)
# # role_home_page = {
# # 	"Role": "home_page"
# # }

# # Generators
# # ----------

# # automatically create page for each record of this doctype
# # website_generators = ["Web Page"]

# # Jinja
# # ----------

# # add methods and filters to jinja environment
# # jinja = {
# # 	"methods": "ui_theme.utils.jinja_methods",
# # 	"filters": "ui_theme.utils.jinja_filters"
# # }

# # Installation
# # ------------

# # before_install = "ui_theme.install.before_install"
# # after_install = "ui_theme.install.after_install"

# # Uninstallation
# # ------------

# # before_uninstall = "ui_theme.uninstall.before_uninstall"
# # after_uninstall = "ui_theme.uninstall.after_uninstall"

# # Integration Setup
# # ------------------
# # To set up dependencies/integrations with other apps
# # Name of the app being installed is passed as an argument

# # before_app_install = "ui_theme.utils.before_app_install"
# # after_app_install = "ui_theme.utils.after_app_install"

# # Integration Cleanup
# # -------------------
# # To clean up dependencies/integrations with other apps
# # Name of the app being uninstalled is passed as an argument

# # before_app_uninstall = "ui_theme.utils.before_app_uninstall"
# # after_app_uninstall = "ui_theme.utils.after_app_uninstall"

# # Desk Notifications
# # ------------------
# # See frappe.core.notifications.get_notification_config

# # notification_config = "ui_theme.notifications.get_notification_config"

# # Permissions
# # -----------
# # Permissions evaluated in scripted ways

# # permission_query_conditions = {
# # 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# # }
# #
# # has_permission = {
# # 	"Event": "frappe.desk.doctype.event.event.has_permission",
# # }

# # DocType Class
# # ---------------
# # Override standard doctype classes

# # override_doctype_class = {
# # 	"ToDo": "custom_app.overrides.CustomToDo"
# # }

# # Document Events
# # ---------------
# # Hook on document methods and events

# # doc_events = {
# # 	"*": {
# # 		"on_update": "method",
# # 		"on_cancel": "method",
# # 		"on_trash": "method"
# # 	}
# # }

# # Scheduled Tasks
# # ---------------

# # scheduler_events = {
# # 	"all": [
# # 		"ui_theme.tasks.all"
# # 	],
# # 	"daily": [
# # 		"ui_theme.tasks.daily"
# # 	],
# # 	"hourly": [
# # 		"ui_theme.tasks.hourly"
# # 	],
# # 	"weekly": [
# # 		"ui_theme.tasks.weekly"
# # 	],
# # 	"monthly": [
# # 		"ui_theme.tasks.monthly"
# # 	],
# # }

# # Testing
# # -------

# # before_tests = "ui_theme.install.before_tests"

# # Overriding Methods
# # ------------------------------
# #
# # override_whitelisted_methods = {
# # 	"frappe.desk.doctype.event.event.get_events": "ui_theme.event.get_events"
# # }
# #
# # each overriding function accepts a `data` argument;
# # generated from the base implementation of the doctype dashboard,
# # along with any modifications made in other Frappe apps
# # override_doctype_dashboards = {
# # 	"Task": "ui_theme.task.get_dashboard_data"
# # }

# # exempt linked doctypes from being automatically cancelled
# #
# # auto_cancel_exempted_doctypes = ["Auto Repeat"]

# # Ignore links to specified DocTypes when deleting documents
# # -----------------------------------------------------------

# # ignore_links_on_delete = ["Communication", "ToDo"]

# # Request Events
# # ----------------
# # before_request = ["ui_theme.utils.before_request"]
# # after_request = ["ui_theme.utils.after_request"]

# # Job Events
# # ----------
# # before_job = ["ui_theme.utils.before_job"]
# # after_job = ["ui_theme.utils.after_job"]

# # User Data Protection
# # --------------------

# # user_data_fields = [
# # 	{
# # 		"doctype": "{doctype_1}",
# # 		"filter_by": "{filter_by}",
# # 		"redact_fields": ["{field_1}", "{field_2}"],
# # 		"partial": 1,
# # 	},
# # 	{
# # 		"doctype": "{doctype_2}",
# # 		"filter_by": "{filter_by}",
# # 		"partial": 1,
# # 	},
# # 	{
# # 		"doctype": "{doctype_3}",
# # 		"strict": False,
# # 	},
# # 	{
# # 		"doctype": "{doctype_4}"
# # 	}
# # ]

# # Authentication and authorization
# # --------------------------------

# # auth_hooks = [
# # 	"ui_theme.auth.validate"
# # ]

# # Automatically update python controller files with type annotations for this app.
# # export_python_type_annotations = True

# # default_log_clearing_doctypes = {
# # 	"Logging DocType Name": 30  # days to retain logs
# # }

app_name = "ui_theme"
app_title = "UI Theme"
app_publisher = "Darshana Patil"
app_description = "Custom UI theme and interface enhancements."
app_email = "darshanap01@brainmine.ai"
app_license = "mit"

# ---------------------------------------------------------
# UI / THEME CONFIGURATION
# ---------------------------------------------------------

# App color (shown in Desk app list if needed)
app_color = "#1F2937"   # You can change this to your brand color


# ---------------------------------------------------------
# DESK (Backend UI) INCLUDES
# ---------------------------------------------------------

# Global CSS for Desk
# app_include_css = [
#     "/assets/ui_theme/css/custom_navbar.css",
#     "/assets/ui_theme/css/home_default.css",
#     "/assets/ui_theme/css/home_sales_user.css",
#     "/assets/ui_theme/css/login_theme.css"
# ]

# Global CSS for Desk
app_include_css = [
    "/assets/ui_theme/css/home_default.css",
    "/assets/ui_theme/css/login_theme.css",
    "/assets/ui_theme/css/home_sales_user.css",
    # Keep navbar overrides last so they win over Frappe/other theme CSS
    "/assets/ui_theme/css/custom_navbar.css?v=20260219_1",
]

# Global JS for Desk
app_include_js = [
    "/assets/ui_theme/js/navbar_brand.js?v=20260219_1",
    "/assets/ui_theme/js/hide_help_menu.js?v=20260219_1",
]




# ---------------------------------------------------------
# LOGIN PAGE CUSTOMIZATION
# ---------------------------------------------------------

# Inject custom login CSS
# website_context = {
#     "add_login_css": "/assets/ui_theme/css/login_theme.css"
# }

# Optional: Explicit login route handling
# website_route_rules = [
#     {"from_route": "/login", "to_route": "login"}
# ]


# ---------------------------------------------------------
# WEBSITE (Optional – if you want website styling)
# ---------------------------------------------------------

# Uncomment if you want website styling also
# web_include_css = [
#     "/assets/ui_theme/css/website_theme.css"
# ]

# web_include_js = [
#     "/assets/ui_theme/js/website_theme.js"
# ]


# ---------------------------------------------------------
# OPTIONAL: SCSS Support (if using SCSS)
# ---------------------------------------------------------

# website_theme_scss = "ui_theme/public/scss/website"


# ---------------------------------------------------------
# APP ICON (Optional)
# ---------------------------------------------------------

# app_include_icons = "ui_theme/public/icons.svg"
