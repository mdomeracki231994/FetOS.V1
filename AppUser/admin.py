from django.contrib import admin

from AppUser.models import AppUser, UserAddress, SocialMediaAccounts

admin.site.register(AppUser)
admin.site.register(UserAddress)
admin.site.register(SocialMediaAccounts)
