from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable1": "This is a variable sent from views",
        "variable2": "This is another variable sent from views"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is Homepage")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is About Page")

def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("This is Contact Page")

def services(request):
    return render(request, 'services.html')