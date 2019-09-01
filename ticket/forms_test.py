from django.test import TestCase
from .forms import TicketCommentForm, TicketCreationForm

class TestTicketCommentForm(TestCase):
    
    def test_users_can_comment(self):
        form = TicketCommentForm({'comment': 'Test comment'})
        self.assertTrue(form.is_valid())
        
    
    def test_form_cant_be_blank(self):
        form = TicketCommentForm({'comment': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['comment'], ['This field is required.'])

        

class TestTicketCreationForm(TestCase):
    
    def test_required_fields(self):
        form = TicketCreationForm({'title':'', 'description': 'Ticket description'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], ['This field is required.'])
        
        form = TicketCreationForm({'title': 'Test title', 'description': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['description'], ['This field is required.'])
        
        
    def test_users_can_create_a_Ticket(self):
        form = TicketCreationForm({'title': 'Ticket Title',
                                'description': 'Ticket description'})
        self.assertTrue(form.is_valid())