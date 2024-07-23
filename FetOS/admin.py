from django.contrib.admin import AdminSite
from django.contrib import admin


class MyAdminSite(AdminSite):
    site_header = "FetOS Admin Site"
    site_title = "FetOS Admin Site"
    index_title = "Welcome to FetOSAdmin"


admin_site = MyAdminSite()

