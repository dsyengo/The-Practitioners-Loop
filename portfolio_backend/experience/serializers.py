from rest_framework import serializers
from .models import Experience

class ExperienceSerializer(serializers.ModelSerializer):
    # This pulls the string from the @property in the model
    period = serializers.CharField(read_only=True) 

    class Meta:
        model = Experience
        fields = [
            'id', 'role', 'company', 'start_date', 'end_date', 
            'is_current', 'period', 'description', 'highlights', 
            'is_published'
        ]