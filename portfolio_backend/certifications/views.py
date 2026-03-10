from rest_framework import viewsets, permissions, filters
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from .models import Certification
from .serializers import CertificationSerializer

# --- DASHBOARD VIEWS (Admin Only) ---

@extend_schema_view(
    list=extend_schema(summary="List all certs/awards", tags=["Dashboard - Certifications"]),
    create=extend_schema(summary="Add new cert/award", tags=["Dashboard - Certifications"]),
)
class DashboardCertificationViewSet(viewsets.ModelViewSet):
    """Manage all certifications and awards."""
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
    permission_classes = [permissions.IsAdminUser]
    
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['type', 'is_published']
    search_fields = ['title', 'issuer', 'description']


# --- PUBLIC VIEWS (Read Only) ---

@extend_schema_view(
    list=extend_schema(summary="List published certs/awards", tags=["Public - Certifications"]),
)
class PublicCertificationViewSet(viewsets.ReadOnlyModelViewSet):
    """Returns only published certifications and awards for the frontend."""
    queryset = Certification.objects.filter(is_published=True)
    serializer_class = CertificationSerializer
    permission_classes = [permissions.AllowAny]
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type'] # Allows frontend to filter just awards or just certs