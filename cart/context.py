from django.shortcuts import get_object_or_404
from ticket.models import Ticket

def cart_contents(request):
    """
    Create a session  of the cart and make it availble to every logged in session 
    Also to appear in every page the user is on
    """
    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    ticket_count = 0
    for id, quantity in cart.items():
        ticket = get_object_or_404(Ticket, pk=id)
        if ticket.paid == True:
            total += quantity * ticket.upvote_price
            ticket_count += quantity
            cart_items.append({'id':id, 'quantity':quantity, 'ticket':ticket})
        else:
            total += quantity * ticket.price
            ticket_count += quantity
            cart_items.append({'id':id, 'quantity':quantity, 'ticket':ticket})

    return {'cart_items':cart_items, 'total':total, 'ticket_count':ticket_count}