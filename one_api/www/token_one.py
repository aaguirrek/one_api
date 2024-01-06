# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals

import frappe
from frappe import _
from frappe.utils.jinja_globals import bundled_asset
from frappe.utils import get_host_name
import requests

no_cache=1
def get_context(context):

    #path_bundle = bundled_asset("frappe-web.bundle.js")
    csrf_token = frappe.sessions.get_csrf_token()
    user = frappe.session.user
    
    url ="https://"+get_host_name()+ bundled_asset("frappe-web.bundle.js")

    payload = ""
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)


    context.csrf_token = csrf_token
    context.user_id = user
    context.path_bundle = response.text
    


#data.elements=frappe.make_get_request("https://dbo.one.com.pe/test_services/api/ApiWeb/ObtenerContenidoWeb",headers = {
#    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IlBhZ2luYSBXZWIgT05FIiwibmJmIjoxNjkzMjUyODU5LCJleHAiOjE5MjQ5MjM2MDAsImlhdCI6MTY5MzI1Mjg1OX0.iDaMQe_13L-jPiZjUbnTEeb-s5ZETIjUKW2dQrg-pwg"
#})