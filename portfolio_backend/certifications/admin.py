from django.contrib import admin
from .models import Certification

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'type', 'date_issued', 'is_published', 'order')
    list_filter = ('type', 'is_published', 'date_issued')
    search_fields = ('title', 'issuer')
    list_editable = ('is_published', 'order')