from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.utils.translation import gettext, gettext_lazy as _

# from .models import *
from .models import UniUser as User


# @admin.register(User)
class UserAdmin(AuthUserAdmin):
    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
        "username",
        "user_type",
        "is_active",
        "is_staff",
        "is_superuser",
        "date_joined",
        "last_login",
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'user_type')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'user_type'),
        }),
    )
    # inlines = (CustomerInline,)


# Re-register UserAdmin
# admin.site.unregister(User)
admin.site.register(User, UserAdmin)
