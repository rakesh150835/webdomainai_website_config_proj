from django.contrib import admin
from .models import Website, WebsiteConfiguration

class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('get_website_name', 'url')  
    search_fields = ('name',)        

    def get_website_name(self, obj):
        if obj.name:
            return obj.name[:30] + '...' if len(obj.name) > 30 else obj.name
    
    get_website_name.short_description = 'Website Name'


# register model here
admin.site.register(Website, WebsiteAdmin)


class WebsiteConfigurationAdmin(admin.ModelAdmin):
    list_display = ('get_website_name', 'get_website_url', 'get_truncated_heading_text', 'color_scheme')  # Fields to display in the list view
    search_fields = ('get_website_url', 'website')

    def get_website_name(self, obj):
        if obj.website.name:
            return obj.website.name[:25] + '...' if len(obj.website.name) > 25 else obj.website.name

    def get_website_url(self, obj):
        return obj.website.url  # Access the 'url' field from the related 'Website' model
    
    def get_truncated_heading_text(self, obj):
        # Limit the number of characters to 30 (or any number you prefer)
        if obj.heading_text:
            return obj.heading_text[:30] + '...' if len(obj.heading_text) > 30 else obj.heading_text

    get_website_name.short_description = 'Website Name'
    get_website_url.short_description = 'Website Url'
    get_truncated_heading_text.short_description = 'heading text'


# register model here
admin.site.register(WebsiteConfiguration, WebsiteConfigurationAdmin)