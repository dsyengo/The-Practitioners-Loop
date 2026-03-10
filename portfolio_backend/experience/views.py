from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from .models import Experience
from .serializers import ExperienceSerializer

# --- DASHBOARD VIEWS (Admin Only) ---

@extend_schema_view(
    list=extend_schema(summary="List all experiences", tags=["Dashboard - Experience"]),
    retrieve=extend_schema(summary="Get experience details", tags=["Dashboard - Experience"]),
    create=extend_schema(summary="Add new experience", tags=["Dashboard - Experience"]),
    update=extend_schema(summary="Update experience", tags=["Dashboard - Experience"]),
    partial_update=extend_schema(summary="Partially update experience", tags=["Dashboard - Experience"]),
    destroy=extend_schema(summary="Delete experience", tags=["Dashboard - Experience"]),
)
class DashboardExperienceViewSet(viewsets.ModelViewSet):
    """Full CRUD access to your work history."""
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.IsAdminUser]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['is_published', 'is_current']
    search_fields = ['role', 'company', 'description']


# --- PUBLIC VIEWS (Read Only) ---

@extend_schema_view(
    list=extend_schema(summary="List published experiences", tags=["Public - Experience"]),
    retrieve=extend_schema(summary="Get published experience details", tags=["Public - Experience"]),
)
class PublicExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    """Returns only published work history for the frontend timeline."""
    queryset = Experience.objects.filter(is_published=True)
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.AllowAny]