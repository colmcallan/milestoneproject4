from django.test import TestCase, Client
from django.contrib import auth
from django.contrib.auth.models import User
from django.test import Client
from .models import Ticket
from django.shortcuts import get_object_or_404


class TestTicketViews(TestCase):
    
    def setUp(self):
        user = User.objects.create_user(username="test", password="testing")
        self.client.login(username="test", password="testing")
        
    def test_all_Ticket_page(self):
        response = self.client.get('/ticket/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Ticket.html')
        
        
    def test_single_Ticket_view(self):
        user = User.objects.get(username="test")
        ticket = Ticket(title="Test title", description="Test description",
                  creator_id=user.id)
        ticket.save()
        response = self.client.get('/ticket/{}'.format(Ticket.id))
        self.assertEqual(response.status_code, 301)
        
    def test_create_Ticket_view(self):
        response = self.client.get('/ticket/create_ticket/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_ticket.html')