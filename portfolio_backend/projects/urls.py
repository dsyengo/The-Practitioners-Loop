from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DashboardProjectViewSet, PublicProjectViewSet

dashboard_router = DefaultRouter()
dashboard_router.register(r'items', DashboardProjectViewSet, basename='dashboard-projects')

public_router = DefaultRouter()
public_router.register(r'items', PublicProjectViewSet, basename='public-projects')

urlpatterns = [
    # Dashboard API (Protected) 
    # Example: /api/projects/dashboard/items/
    path('dashboard/', include(dashboard_router.urls)),
    
    # Public API (Read-Only)
    # Example: /api/projects/public/items/
    path('public/', include(public_router.urls)),
]