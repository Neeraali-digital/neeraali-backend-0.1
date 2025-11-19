from django.db import models

class Service(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    features = models.JSONField(default=list)  # List of features
    price = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    # Dynamic sections for service detail page
    hero_section = models.JSONField(default=dict, blank=True)  # {title, subtitle, description, button_text}
    services_section = models.JSONField(default=list, blank=True)  # List of {icon, title, description}
    faq_section = models.JSONField(default=list, blank=True)  # List of {question, answer}
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', '-created_at']
