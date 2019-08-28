from django.shortcuts import render
from bug.models import Bug
from ticket.models import Ticket

# Create your views here.
def search(request):
    bug = Bug.objects.filter(title__icontains=request.GET['q'])
    ticket = Ticket.objects.filter(title__icontains=request.GET['q'], paid=True)
    bug_count = bug.count()
    ticket_count = ticket.count()
    
    context = {
        'bug': bug,
        'ticket': ticket,
        'bug_count': bug_count,
        'ticket_count': ticket_count,
    }
    return render(request, "search.html", context)