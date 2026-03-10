from django.db import models
from django.utils import timezone

class Experience(models.Model):
    role = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    
    # Using dates allows the database to sort your jobs accurately
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Leave blank if this is your current role")
    is_current = models.BooleanField(default=False)
    
    description = models.TextField()
    
    # Stores data as an array: ["System Reliability", "Automation", "Operational Support"]
    highlights = models.JSONField(default=list, help_text="List of key achievements/skills")
    
    is_published = models.BooleanField(default=True)
    created_when = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Sorts by most recent jobs first
        ordering = ['-start_date']
        verbose_name_plural = "Experiences"

    @property
    def period(self):
        """Automatically formats the period string for the frontend."""
        start_str = self.start_date.strftime("%b %Y")
        if self.is_current or not self.end_date:
            end_str = "Present"
        else:
            end_str = self.end_date.strftime("%b %Y")
        return f"{start_str} - {end_str}"

    def __str__(self):
        return f"{self.role} at {self.company}"