from django.db import models

class Certification(models.Model):
    TYPE_CHOICES = (
        ('certification', 'Certification'),
        ('award', 'Award / Honor'),
    )

    title = models.CharField(max_length=255)
    issuer = models.CharField(max_length=255, help_text="e.g., Coursera, AWS, HackerRank")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='certification')
    
    date_issued = models.DateField()
    
    # Optional fields for verification and display
    credential_url = models.URLField(blank=True, null=True, help_text="Link to verify the certificate")
    image = models.ImageField(upload_to='certifications/', blank=True, null=True)
    description = models.TextField(blank=True, help_text="Brief details about what the certification covers")
    
    is_published = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first")

    class Meta:
        # Sort by manual order first, then by the most recently issued
        ordering = ['order', '-date_issued']

    def __str__(self):
        return f"{self.title} from {self.issuer}"