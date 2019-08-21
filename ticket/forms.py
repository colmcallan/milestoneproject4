from django import forms
from .models import FeatureComment, Feature

class TicketCommentForm(forms.ModelForm):
    class Meta:
        model = TicketComment
        fields = ('comment',)
        
class TicketCreationForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'description')