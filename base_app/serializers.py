from rest_framework import serializers
from .models import WebsiteConfiguration

class WebsiteConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteConfiguration
        fields = ['chat_bot_image', 'heading_text', 'welcome_message', 'send_message_icon', 'color_scheme']
        
    