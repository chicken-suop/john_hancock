# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "john_hancock"
app_title = "John Hancock"
app_publisher = "_ratskin_"
app_description = "Are you in the market for a new signature app??? \n Well, guess what I have for YOU. \n That's right, this is... (DUN DUN DUUUUN!!!) the best amalgamation of eSigning software, EVER!"
app_icon = "octicon octicon-checklist"
app_color = "red"
app_email = "elliot.schep@gmail.com"
app_license = ""

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/john_hancock/css/john_hancock.css"
# app_include_js = "/assets/john_hancock/js/john_hancock.js"

# include js, css files in header of web template
# web_include_css = "/assets/john_hancock/css/john_hancock.css"
# web_include_js = "/assets/john_hancock/js/john_hancock.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#   "Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "john_hancock.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "john_hancock.install.before_install"
# after_install = "john_hancock.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "john_hancock.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#   "Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#   "Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#   "*": {
#       "on_update": "method",
#       "on_cancel": "method",
#       "on_trash": "method"
#   }
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#     "hourly": [
#         "john_hancock.tasks.update_hourly"
#     ],
#     "daily": [
#         "john_hancock.task.update_daily"
#     ],
#     "weekly": [
#         "john_hancock.task.update_weekly"
#     ],
# }

# Testing
# -------

# before_tests = "john_hancock.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
#   "frappe.desk.doctype.event.event.get_events": "john_hancock.event.get_events"
# }
