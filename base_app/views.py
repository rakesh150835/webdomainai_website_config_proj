from django.shortcuts import render, redirect, get_object_or_404
from base_app.models import Website, WebsiteConfiguration
from .serializers import WebsiteConfigSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    websites = Website.objects.all()

    context = {
        'websites': websites,
    }
    return render(request, 'base_app/index.html', context)



@login_required
def add_website(request):
    websites = Website.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        url = request.POST.get('url')
        background_image = request.FILES.get('background_image')

        if Website.objects.filter(name=name).exists():
            return render(request, 'base_app/index.html', {
                'error': 'A website with this name already exists.',
                'websites': websites,
            })

        if Website.objects.filter(url=url).exists():
            return render(request, 'base_app/index.html', {
                'error': 'A website with this URL already exists.',
                'websites': websites,
            })

        try:
            Website.objects.create(
                            name=name,
                            url=url,
                            background_image=background_image
                        )
            return redirect('home')

        except Exception as e:
            return render(request, 'base_app/index.html', {
                'error': 'There was a problem saving the data. Please ensure the data is correct and unique.',
                'websites': websites,
            })
            
    return render(request, 'base_app/index.html', {'websites': websites})


@login_required
def add_website_configuration(request, website_id=None):
    if website_id:
        website = get_object_or_404(Website, pk=website_id)  # Fetch existing website to update
        websiteConfig = website.websiteconfiguration
    else:
        websiteConfig = WebsiteConfiguration()

    if request.method == 'POST':
        websiteConfig.heading_text = request.POST.get('heading_text')
        websiteConfig.welcome_message = request.POST.get('welcome_message')
        
        if 'chatbot_image' in request.FILES:
            websiteConfig.chat_bot_image = request.FILES.get('chatbot_image')
        if 'send_message_icon' in request.FILES:
            websiteConfig.send_message_icon = request.FILES.get('send_message_icon')

        websiteConfig.color_scheme = request.POST.get('color_scheme')
        print("color sceme:  --", request.POST.get('color_scheme'))
        try:
            websiteConfig.save()
            return redirect('home')

        except Exception as e:
            return render(request, 'base_app/WebsiteConfiguration.html', {
                'error': 'There was a problem saving the data. Please ensure the data is unique.',
                'websiteConfig': websiteConfig,
            })
            
    return render(request, 'base_app/WebsiteConfiguration.html', {'websiteConfig': websiteConfig})



@api_view(['GET'])
def search_by_url(request):
    url_param = request.GET.get('url')

    if url_param:
        website = Website.objects.filter(url__icontains=url_param).first()

        if website:
            website_config = WebsiteConfiguration.objects.filter(website=website).first()

            if website_config:
                # Serialize the WebsiteConfiguration object
                serializer = WebsiteConfigSerializer(website_config)
                print("serializer data:- ", serializer.data)
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response({'error': 'Website configuration not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'error': 'Website not found'}, status=status.HTTP_404_NOT_FOUND)

    return Response({'error': 'URL parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
