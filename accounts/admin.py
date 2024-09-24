from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .forms import UserChangeForm, UserCreationForm




class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    list_display = ('email', 'first_name', 'is_admin', 'is_staff')
    list_filter = ["is_admin", "is_staff"]
    
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["first_name", "last_name"]}),
        ("Permissions", {"fields": ["is_admin", "is_active", "is_staff", "is_superuser"]}),
    ]
     
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "first_name", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email", "first_name"]
    ordering = ["email"]
    filter_horizontal = []


# register the new UserAdmin
admin.site.register(User, UserAdmin)





