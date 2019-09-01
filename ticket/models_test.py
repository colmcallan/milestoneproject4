from django.test import TestCase
from .models import Ticket, TicketComment


class TicketEntryTest(TestCase):
    
    def test_string_representation(self):
        ticket = Ticket(title="TestTicket")
        self.assertEqual(str(Ticket), Ticket.title)