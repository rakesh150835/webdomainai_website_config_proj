from django.contrib import admin
from .models import Website, WebsiteConfiguration

class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')  # Fields to display in the list view
    search_fields = ('name',)        # Fields to search in the admin



class WebsiteConfigurationAdmin(admin.ModelAdmin):
    list_display = ('website', 'get_website_url', 'get_truncated_heading_text', 'color_scheme')  # Fields to display in the list view
    search_fields = ('get_website_url', 'website')

    def get_website_url(self, obj):
        return obj.website.url  # Access the 'url' field from the related 'Website' model
    
    def get_truncated_heading_text(self, obj):
        # Limit the number of characters to 30 (or any number you prefer)
        if obj.heading_text:
            return obj.heading_text[:30] + '...' if len(obj.heading_text) > 30 else obj.heading_text

    get_website_url.short_description = 'Website Url'
    get_truncated_heading_text.short_description = 'heading text'



admin.site.register(Website, WebsiteAdmin)
admin.site.register(WebsiteConfiguration, WebsiteConfigurationAdmin)