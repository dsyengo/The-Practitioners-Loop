from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    CATEGORY_CHOICES = (
        ('design', 'Design (UI/UX, Figma)'),
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('fullstack', 'Fullstack'),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='fullstack')
    
    description = models.TextField()
    my_contributions = models.TextField(help_text="Detail your specific roles and achievements here.")
    
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    
    # Stores data exactly as your frontend expects: ["Node.js", "React", "MongoDB"]
    tags = models.JSONField(default=list, help_text="List of technologies used")
    
    code_link = models.URLField(blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)
    
    is_published = models.BooleanField(default=True)
    created_when = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first")

    class Meta:
        ordering = ['order', '-created_when']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title