from django.contrib import admin
from basic_app.models import UserProfileInfo
# Register your models here.

class UserProfileInfoAdmin(admin.ModelAdmin):
	list_display=['user']

admin.site.register(UserProfileInfo,UserProfileInfoAdmin)
