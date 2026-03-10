from rest_framework import viewsets, permissions, filters
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from .models import Category, BlogPost
from .serializers import CategorySerializer, BlogPostSerializer

# --- DASHBOARD VIEWS (Admin Only) ---

@extend_schema_view(
    list=extend_schema(summary="List all categories", tags=["Dashboard - Categories"]),
    retrieve=extend_schema(summary="Get category details", tags=["Dashboard - Categories"]),
    create=extend_schema(summary="Create new category", tags=["Dashboard - Categories"]),
    update=extend_schema(summary="Update category", tags=["Dashboard - Categories"]),
    partial_update=extend_schema(summary="Partially update category", tags=["Dashboard - Categories"]),
    destroy=extend_schema(summary="Delete category", tags=["Dashboard - Categories"]),
)
class DashboardCategoryViewSet(viewsets.ModelViewSet):
    """Manage blog categories from the dashboard."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


@extend_schema_view(
    list=extend_schema(summary="List all blogs (Dashboard)", tags=["Dashboard - Blogs"]),
    retrieve=extend_schema(summary="Get blog details", tags=["Dashboard - Blogs"]),
    create=extend_schema(summary="Create new blog", tags=["Dashboard - Blogs"]),
    update=extend_schema(summary="Update blog", tags=["Dashboard - Blogs"]),
    partial_update=extend_schema(summary="Partially update blog", tags=["Dashboard - Blogs"]),
    destroy=extend_schema(summary="Delete blog", tags=["Dashboard - Blogs"]),
)
class DashboardBlogPostViewSet(viewsets.ModelViewSet):
    """Full CRUD access to all blog posts, including drafts and image uploads."""
    queryset = BlogPost.objects.all().order_by('-created_when')
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAdminUser]
    
    # Enable form parsing to accept image uploads alongside JSON data
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'category']
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        # Automatically set the author to the logged-in admin user
        serializer.save(author=self.request.user)


# --- PUBLIC VIEWS (Read Only) ---

@extend_schema_view(
    list=extend_schema(summary="List published blogs", tags=["Public - Blogs"]),
    retrieve=extend_schema(summary="Get published blog details", tags=["Public - Blogs"]),
)
class PublicBlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    """Only returns blogs where status is 'published'."""
    queryset = BlogPost.objects.filter(status='published').order_by('-created_when')
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.AllowAny]
    
    # Allows the frontend to fetch a post by its slug (e.g., /api/public/blogs/my-first-post/)
    lookup_field = 'slug'


@extend_schema_view(
    list=extend_schema(summary="List categories", tags=["Public -  Blogs Categories"]),
    retrieve=extend_schema(summary="Get category details", tags=["Public - Blogs Categories"]),
)
class PublicCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Public read-only categories for frontend filtering."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]