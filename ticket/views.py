from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Ticket, TicketComment
from django.utils import timezone
from django.contrib import messages
from .forms import TicketCommentForm, TicketCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def show_all_tickets(request):
    """
    View to show all our tickets on
    one page
    """
    tickets = Ticket.objects.filter(created_date__lte=timezone.now(), paid=True)
    
    context = {
        'tickets': tickets
    }
    return render(request, 'tickets.html', context)
    

def single_ticket_view(request, pk):
    """
    Route to view a single ticket on
    one page
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    
    if request.method == 'POST':
        ticket_comment_form = TicketCommentForm(request.POST or None)
        if ticket_comment_form.is_valid():
            comment = request.POST.get('comment')
            ticket_comment = TicketComment.objects.create(ticket=ticket, creator=request.user, comment=comment)
            ticket_comment.save()
            messages.success(request, 'Thanks {} your comment has posted'.format(request.user), extra_tags="alert-success")
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        ticket_comment_form = TicketCommentForm()
        ticket.views += 1
        ticket.save()
    
    comments = TicketComment.objects.filter(ticket=ticket)
    
    ticket_comment_form = TicketCommentForm()
            
    context = {
        'ticket' : ticket,
        'ticket_comment_form': ticket_comment_form,
        'comments': comments,
    }
    
    
    return render(request, 'single_ticket.html', context)
    
@login_required
def edit_a_ticket(request, pk):
    """
    Route to allow users to edit their bug
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    
    if request.method == "POST":
        form = TicketCreationForm(request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.creator = request.user
            ticket.save()
            messages.success(request, "Thanks {0}, {1} has been updated."
                             .format(request.user, ticket.title),
                             extra_tags="alert-success")
            return redirect(reverse('profile'))
    
    else:
        form = TicketCreationForm(instance=ticket)
        
    context = {
        'form': form,
    }
    return render(request, 'edit_ticket.html', context)
    
 
@login_required
def create_a_ticket(request):
    form = TicketCreationForm(request.POST)
    if request.method == "POST":
        
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.creator = request.user
            ticket.save()
            
            cart = request.session.get('cart', {})
            id = ticket.id
            cart[id] = cart.get(id, 1)
            request.session['cart'] = cart
            return redirect('checkout')
    else:
        form = TicketCreationForm()
    
    context = {
        'form' : form
    }
    
    return render(request, 'create_ticket.html', context)


@login_required
def delete_a_ticket(request, pk):
    """
    Route to allow users to delete their tickets
    """
    
    ticket = get_object_or_404(Ticket, pk=pk)
    
    if request.method == "POST":
        ticket.delete()
        messages.success(request, '{} your ticket has been deleted!'.format(request.user), extra_tags="alert-success")
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, '{} unfortunatley at this time your ticket cannot be deleted.'.format(request.user), extra_tags="alert-primary")
        return redirect(request.META.get('HTTP_REFERER'))