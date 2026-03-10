from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    # Columns to show in the list view
    list_display = ('name', 'email', 'subject', 'created_at', 'is_processed')
    
    # Add a sidebar filter for processed/unprocessed messages
    list_filter = ('is_processed', 'created_at')
    
    # Add a search bar for names and emails
    search_fields = ('name', 'email', 'subject', 'message')
    
    # Order by newest first
    ordering = ('-created_at',)
    
    # Make the 'is_processed' field editable directly in the list
    list_editable = ('is_processed',)