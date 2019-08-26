from django.conf.urls import url
from .views import show_all_tickets, single_ticket_view, create_a_ticket, delete_a_ticket, edit_a_ticket

urlpatterns = [
    url(r'^$', show_all_tickets, name="show_all_tickets"),
    url(r'^(?P<pk>\d+)/$', single_ticket_view, name="single_ticket_view"),
    url(r'^(?P<pk>\d+)/delete_ticket/$', delete_a_ticket, name="delete_a_ticket"),
    url(r'^(?P<pk>\d+)/edit_a_ticket/$', edit_a_ticket, name="edit_a_ticket"),
    url(r'^create_ticket/$', create_a_ticket, name='create_a_ticket'),
    ]