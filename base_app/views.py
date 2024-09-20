from django.shortcuts import render, redirect
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


def resize_image(image, size=(100, 100)):
    img = Image.open(image)
    img.thumbnail(size)
    img_io = BytesIO()
    img.save(img_io, format='JPEG', quality=85)
    return ContentFile(img_io.getvalue(), name=image.name)


def add_website(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        url = request.POST.get('url')
        background_image = request.FILES.get('background_image')
        resized_image = resize_image(background_image)

        Website.objects.create(
            name=name,
            url=url,
            background_image=resized_image
        )
        return redirect('home')  

    return render(request, 'add_website.html')



def add_website_configuration(request):
    if request.method == 'POST':
        licence_key = request.POST.get('licence_key')
        heading_text = request.POST.get('heading_text')
        welcome_message = request.POST.get('welcome_message')
        chatbot_image = request.FILES.get('chatbot_image')
        send_message_icon = request.FILES.get('send_message_icon')
        send_message_icon = request.FILES.get('color_scheme')
        
        WebsiteConfiguration.objects.create(
            licence_key=licence_key,
            chatbot_image=chatbot_image,
            heading_text=heading_text,
            welcome_message=welcome_message,
            send_message_icon=send_message_icon,
            color_scheme=color_scheme
        )
        
        return redirect('home')  

    return render(request, 'WebsiteConfiguration.html')
