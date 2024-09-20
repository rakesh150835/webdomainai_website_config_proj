from django.contrib import admin
from .models import Website, WebsiteConfiguration

class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')  # Fields to display in the list view
    search_fields = ('name',)        # Fields to search in the admin



class WebsiteConfigurationAdmin(admin.ModelAdmin):
    list_display = ('website', 'licence_key', 'heading_text', 'color_scheme')  # Fields to display in the list view
    search_fields = ('licence_key', 'website')




admin.site.register(Website, WebsiteAdmin)
admin.site.register(WebsiteConfiguration, WebsiteConfigurationAdmin)