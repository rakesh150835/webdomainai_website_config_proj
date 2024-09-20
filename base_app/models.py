from django.db import models

# Create your models here.

class Website(models.Model):
    name = models.CharField(max_length=200, unique=True)
    url = models.URLField(max_length=255, unique=True)
    background_image = models.ImageField(upload_to='bg_images/')

    
    def __str__(self):
        return self.name



class WebsiteConfiguration(models.Model):
    website = models.OneToOneField(Website, on_delete=models.CASCADE)
    licence_key = models.CharField(max_length=250, unique=True)
    chatbot_image = models.ImageField(upload_to='chatbot_images/')
    heading_text = models.CharField(max_length=500)
    welcome_message = models.TextField()
    send_message_icon = models.ImageField(upload_to='send_message_icons/')
    color_scheme = models.CharField(max_length=7)

    
    def __str__(self):
        return self.licence_key

