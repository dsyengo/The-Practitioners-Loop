from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DashboardExperienceViewSet, PublicExperienceViewSet

dashboard_router = DefaultRouter()
dashboard_router.register(r'items', DashboardExperienceViewSet, basename='dashboard-experience')

public_router = DefaultRouter()
public_router.register(r'items', PublicExperienceViewSet, basename='public-experience')

urlpatterns = [
    # Dashboard API (Protected) 
    # Example: /api/experience/dashboard/items/
    path('dashboard/', include(dashboard_router.urls)),
    
    # Public API (Read-Only)
    # Example: /api/experience/public/items/
    path('public/', include(public_router.urls)),
]