from django.contrib import admin

from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'is_admin', 'is_staff')  # Fields to display in the list view
    search_fields = ('email','is_admin', 'is_staff')


admin.site.register(User, UserAdmin)