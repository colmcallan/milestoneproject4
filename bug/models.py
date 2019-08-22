from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Bug(models.Model):
    """A Bugs Post
    Status choices, including user upvotes(how to purchase)
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
    bug_upvotes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-bug_upvotes']
    
    
    def __str__(self):
        return self.title
        

class upVotes(models.Model):
    """Bug upvotes"""
    upvote_user = models.ForeignKey(User, on_delete=models.CASCADE)
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Up votes"
    
    def __str__(self):
        return self.upvote_user.username
        

class BugComment(models.Model):
    """Bug Comments"""
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=256, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return '{0}: {1}'.format(self.bug.title, self.creator.username)