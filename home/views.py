from django.shortcuts import render

# Create your views here.
def index(request):
    """
    A view that displays the index page 
    """
    return render(request, "index.html")
    
def faq(request):
    """
    A view that display the faq page
    """
    return render(request, "faq.html")
    
