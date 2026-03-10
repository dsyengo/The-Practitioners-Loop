from django.contrib import admin
from .models import Experience

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'start_date', 'is_current', 'is_published')
    list_filter = ('is_current', 'is_published')
    search_fields = ('role', 'company', 'description', 'highlights')
    list_editable = ('is_current', 'is_published')