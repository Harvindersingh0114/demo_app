# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "demo_app",
			"color": "#000000",
			"icon": "Harry",
			"type": "module",
			"label": _("demo_app")
		}
	]
