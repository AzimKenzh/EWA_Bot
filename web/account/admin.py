from django.contrib import admin

from account.models import MyUser, Status

admin.site.register(MyUser)
admin.site.register(Status)