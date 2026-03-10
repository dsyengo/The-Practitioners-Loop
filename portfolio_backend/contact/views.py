from django.db import transaction
from rest_framework import generics, status
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from drf_spectacular.utils import extend_schema, OpenApiResponse
from .models import ContactMessage
from .serializers import ContactMessageSerializer

@extend_schema(
    tags=["Public - Contact"],
    summary="Submit a contact message",
    description="Sends an email and saves the message to the database only if the email is successful.",
    request=ContactMessageSerializer,
    responses={
        201: OpenApiResponse(
            description="Email sent and message saved.",
            response={"type": "object", "properties": {"detail": {"type": "string"}}}
        ),
        400: OpenApiResponse(
            description="Validation error.",
            response={"type": "object", "properties": {"error": {"type": "string"}}}
        ),
        500: OpenApiResponse(
            description="Email service failure.",
            response={"type": "object", "properties": {"error": {"type": "string"}}}
        )
    }
)
class ContactMessageCreateView(generics.CreateAPIView):
    """
    Endpoint for submitting contact form messages.
    
    This endpoint:
    * Validates the incoming contact form data
    * Attempts to send an email notification
    * Only saves to database if email is sent successfully
    * Uses database transactions to ensure data consistency
    """
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Extract data
        name = serializer.validated_data.get('name')
        sender_email = serializer.validated_data.get('email')
        subject = serializer.validated_data.get('subject')
        message = serializer.validated_data.get('message')

        email_subject = f"Portfolio Contact: {subject}"
        email_body = f"""
New message from {name} ({sender_email}):

Subject: {subject}

Message:
{message}
        """.strip()

        # Use an atomic transaction to ensure DB and Email sync
        try:
            with transaction.atomic():
                # 1. Send the email first
                # If this fails, it jumps to the 'except' block and the DB save never happens
                send_mail(
                    subject=email_subject,
                    message=email_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )

                # 2. Save to database only if send_mail didn't crash
                self.perform_create(serializer)

            return Response(
                {"detail": "Your message has been sent and recorded successfully!"},
                status=status.HTTP_201_CREATED
            )

        except Exception as e:
            # Log the error here if you have a logger
            # logger.error(f"Contact form error: {str(e)}")
            return Response(
                {"error": "Message could not be sent. Please try again later."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )