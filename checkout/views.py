from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from ticket.models import Ticket
import stripe


# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    """View to allow users to pay for ticket upvotes"""
    cart = request.session.get('cart', {})
    for id, quantity in cart.items():
        ticket = get_object_or_404(Ticket, pk=id)
    
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            total = 0
            for id, quantity in cart.items():
                total += quantity * ticket.price
                order_line_item = OrderLineItem(
                    order = order, 
                    ticket = ticket, 
                    creator = request.user
                    )
                order_line_item.save()
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!", extra_tags="alert-primary")
            if customer.paid:
                for id, quantity in cart.items():
                    if ticket.paid == False:
                        ticket.paid = True
                    elif ticket.paid == True:
                        ticket.ticket_upvotes += quantity
                    ticket.save()
                messages.error(request, "You have successfully paid", extra_tags="alert-success")
                request.session['cart'] = {}
                return redirect(reverse('show_all_ticket'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!", extra_tags="alert-primary")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
                
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
