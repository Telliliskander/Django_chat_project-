from django.shortcuts import render

# Create your views here.

def message_page(request):
    return render(request, 'start_point_messages.html') 
