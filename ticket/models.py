from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.
class Ticket(models.Model):
    """A ticket post
    To be pulled into forms for creating ticket to be raised and paid for
    """
    STATUS_CHOICES = (
        ('To do', 'To do'),
        ('In progress', 'In progress'),
        ('Complete', 'Complete')
        )


    title = models.CharField(max_length=56, blank=False)
    description = models.TextField(blank=False)
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES,
                              default='To do')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    price = models.IntegerField(default=20, blank=False)
    ticket_upvotes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    upvote_price = models.IntegerField(default=5, blank=False)
    
    class Meta:
        ordering = ['-ticket_upvotes']
    
    
    def __str__(self):
        return self.title
        

class TicketComment(models.Model):
    """Ticket Comments by other users and creator"""
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=256, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return '{0}: {1}'.format(self.ticket.title, self.creator.username)