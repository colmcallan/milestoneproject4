from django.contrib import admin
from .models import Ticket, TicketComment

# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status', 'creator',
                    'created_date', 'ticket_upvotes']
    list_filter = ('status',)
    
class TicketCommentAdmin(admin.ModelAdmin):
    list_display = ['ticket', 'comment', 'creator', 'created_date']
    list_filter = ('ticket', 'creator')

admin.site.register(Ticket, TicketAdmin)
admin.site.register(TicketComment, TicketCommentAdmin)