from rest_framework import viewsets, permissions, filters
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from .models import Project
from .serializers import ProjectSerializer

# --- DASHBOARD VIEWS (Admin Only) ---

@extend_schema_view(
    list=extend_schema(summary="List all projects", tags=["Dashboard - Projects"]),
    retrieve=extend_schema(summary="Get project details", tags=["Dashboard - Projects"]),
    create=extend_schema(summary="Create a new project", tags=["Dashboard - Projects"]),
    update=extend_schema(summary="Update project", tags=["Dashboard - Projects"]),
    partial_update=extend_schema(summary="Partially update project", tags=["Dashboard - Projects"]),
    destroy=extend_schema(summary="Delete project", tags=["Dashboard - Projects"]),
)
class DashboardProjectViewSet(viewsets.ModelViewSet):
    """Full CRUD access to all projects, including unpublished ones."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAdminUser]
    
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'is_published']
    search_fields = ['title', 'description', 'my_contributions']


# --- PUBLIC VIEWS (Read Only) ---

@extend_schema_view(
    list=extend_schema(summary="List published projects", tags=["Public - Projects"]),
    retrieve=extend_schema(summary="Get project details", tags=["Public - Projects"]),
)
class PublicProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """Returns only published projects for the frontend."""
    queryset = Project.objects.filter(is_published=True)
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']  # Allows frontend to filter by /projects/?category=frontend
    lookup_field = 'slug'