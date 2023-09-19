from django.contrib import admin
from App_Account.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "first_name", "last_name", "mobile"]


admin.site.register(User, UserAdmin)
