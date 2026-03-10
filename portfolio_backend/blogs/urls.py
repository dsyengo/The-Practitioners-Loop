from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DashboardCategoryViewSet,
    DashboardBlogPostViewSet,
    PublicBlogPostViewSet,
    PublicCategoryViewSet
)

# 1. Dashboard Router (Protected Admin Routes)
dashboard_router = DefaultRouter()
dashboard_router.register(r'categories', DashboardCategoryViewSet, basename='dashboard-categories')
dashboard_router.register(r'posts', DashboardBlogPostViewSet, basename='dashboard-blogs')

# 2. Public Router (Read-Only/Open Routes)
public_router = DefaultRouter()
public_router.register(r'categories', PublicCategoryViewSet, basename='public-categories')
public_router.register(r'posts', PublicBlogPostViewSet, basename='public-blogs')

urlpatterns = [
    # Dashboard API (Private) 
    # Example: /blogs/dashboard/posts/
    path('dashboard/', include(dashboard_router.urls)),
    
    # Public API (Read-Only)
    # Example: /blogs/public/posts/
    path('public/', include(public_router.urls)),
]