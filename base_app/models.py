from django.db import models

# Create your models here.

class Website(models.Model):
    name = models.CharField(max_length=200, unique=True)
    url = models.URLField(max_length=255, unique=True)
    background_image = models.ImageField(upload_to='bg_images/')

    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Call the original save method
        super().save(*args, **kwargs)
        # Create a UserProfile instance if it doesn't exist
        WebsiteConfiguration.objects.get_or_create(website=self)

    



class WebsiteConfiguration(models.Model):
    website = models.OneToOneField(Website, on_delete=models.CASCADE)
    chat_bot_image = models.ImageField(upload_to='chatbot_images/')
    heading_text = models.CharField(max_length=500, null=True, blank=True)
    welcome_message = models.TextField(max_length=700, null=True, blank=True)
    send_message_icon = models.ImageField(upload_to='send_message_icons/')
    color_scheme = models.CharField(max_length=7, null=True, blank=True)

    
    def __str__(self):
        return self.website.name
