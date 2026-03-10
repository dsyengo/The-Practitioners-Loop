from rest_framework import serializers
from .models import Certification

class CertificationSerializer(serializers.ModelSerializer):
    # Format the date nicely for the frontend (e.g., "March 2026")
    formatted_date = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Certification
        fields = [
            'id', 'title', 'issuer', 'type', 'date_issued', 
            'formatted_date', 'credential_url', 'image', 
            'description', 'is_published', 'order'
        ]

    def get_formatted_date(self, obj):
        return obj.date_issued.strftime("%B %Y")