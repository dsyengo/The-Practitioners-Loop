from django.http import JsonResponse
from django.db import connection
from django.core.cache import cache
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import time

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import AuthenticationFailed
from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers

@extend_schema(
    summary="API Health Check",
    description="Checks the status of the backend, database, and cache systems.",
    responses={
        200: OpenApiResponse(description="System is healthy"),
        503: OpenApiResponse(description="One or more services are unavailable")
    }
)
@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    health_status = {
        "status": "online",
        "timestamp": time.time(),
        "services": {
            "database": "unhealthy",
            "cache": "unhealthy"
        }
    }
    
    overall_healthy = True

    # 1. Database Check
    try:
        connection.ensure_connection()
        health_status["services"]["database"] = "healthy"
    except Exception as e:
        overall_healthy = False
        health_status["services"]["database"] = f"unhealthy: {str(e)}"

    # 2. Cache Check (Optional - good if you use Redis/Memcached)
    try:
        cache.set('health_check', 'ok', timeout=5)
        if cache.get('health_check') == 'ok':
            health_status["services"]["cache"] = "healthy"
        else:
            health_status["services"]["cache"] = "unhealthy"
    except Exception:
        # We don't necessarily fail the whole app if cache is down, 
        # but you can toggle overall_healthy = False here if it's critical.
        health_status["services"]["cache"] = "unavailable"

    # Set overall status
    if not overall_healthy:
        health_status["status"] = "degraded"
        return JsonResponse(health_status, status=503)

    return JsonResponse(health_status, status=200)

class AdminTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # This standard call verifies the username and password
        data = super().validate(attrs)
        
        # Check if the authenticated user is an admin
        if not self.user.is_staff and not self.user.is_superuser:
            raise AuthenticationFailed(
                "Access denied: Only administrators can log in to the dashboard.", 
                code='authorization'
            )
        
        # Optional: Attach extra user details to the response payload for your frontend
        data['username'] = self.user.username
        data['email'] = self.user.email
        
        return data

@extend_schema(tags=["Authentication"], summary="Dashboard Login (Admin Only)")
class AdminLoginView(TokenObtainPairView):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token to prove the authentication of those credentials. Only allows staff/superusers.
    """
    serializer_class = AdminTokenObtainPairSerializer
    
    
class AdminLogoutView(APIView):
    # Only authenticated users can log out
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Authentication"],
        summary="Dashboard Logout",
        description="Logs out the user by blacklisting the provided refresh token.",
        request=inline_serializer(
            name="LogoutRequest",
            fields={"refresh": serializers.CharField(help_text="The refresh token to blacklist.")}
        ),
        responses={
            205: OpenApiResponse(description="Successfully logged out."),
            400: OpenApiResponse(description="Bad request (e.g., invalid or missing token).")
        }
    )
    def post(self, request):
        try:
            # 1. Get the refresh token from the request body
            refresh_token = request.data.get("refresh")
            
            if not refresh_token:
                return Response({"error": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)

            # 2. Instantiate the token and blacklist it
            token = RefreshToken(refresh_token)
            token.blacklist()

            # 205 Reset Content tells the client to clear its current view/data
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
            
        except Exception as e:
            # If the token is already blacklisted or invalid, it will throw an error
            return Response({"error": "Token is invalid or already logged out."}, status=status.HTTP_400_BAD_REQUEST)