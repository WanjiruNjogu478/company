from django.shortcuts import render

def home(request):
    context = {
        'title': 'Welcome to My Website',
        'content': 'This is a dynamic content area.'
    }
    return render(request, 'index.html', context)



