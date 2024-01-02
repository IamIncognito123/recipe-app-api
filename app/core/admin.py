"""
Django admin customization
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# allows for wrapping of text/sections to be translated in other languages
from django.utils.translation import gettext_lazy as _

# Register your models here.

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    # ordering displays data associated in ascending order of 'id'
    # list display, displays the corresponding data of the ids
    # fieldsets allows for customization of how fields are displayed using tuples
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important Dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )

admin.site.register(models.User, UserAdmin)