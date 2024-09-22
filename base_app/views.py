from django.shortcuts import render, redirect, get_object_or_404
from .models import Website, WebsiteConfiguration

from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO



def home(request):
    websites = Website.objects.all()

    context = {
        'websites': websites,
    }
    return render(request, 'base_app/index.html', context)




def add_website(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        url = request.POST.get('url')
        background_image = request.FILES.get('background_image')

        Website.objects.create(
            name=name,
            url=url,
            background_image=background_image
        )
        return redirect('home')  

    return render(request, 'add_website.html')



def add_website_configuration(request, website_id=None):
    if website_id:
        website = get_object_or_404(Website, pk=website_id)  # Fetch existing website to update

        websiteConfig = website.websiteconfiguration
        #print("web confi heading_text-----", websiteConfig.heading_text)
    else:
        websiteConfig = WebsiteConfiguration()

    if request.method == 'POST':
        websiteConfig.licence_key = request.POST.get('licence_key')
        websiteConfig.heading_text = request.POST.get('heading_text')
        websiteConfig.welcome_message = request.POST.get('welcome_message')
        
        if 'background_image' in request.FILES:
            websiteConfig.chatbot_image = request.FILES.get('chatbot_image')
        if 'background_image' in request.FILES:
            websiteConfig.send_message_icon = request.FILES.get('send_message_icon')

        websiteConfig.color_scheme = request.POST.get('color_scheme')
        
        websiteConfig.save()
        
        return redirect('home')  

    #print("website configuration:  ", websiteConfig)
    return render(request, 'base_app/WebsiteConfiguration.html', {'websiteconfig': websiteConfig})
