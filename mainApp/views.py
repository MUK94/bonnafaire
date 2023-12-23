from django.shortcuts import render

def index(request):
    context = {
        'welcome_message': 'Welcome to our B2B2C Platform!',     
    }
    return render(request, 'index.html', context)
