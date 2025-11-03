from django.db import models

class Job(models.Model):
    TYPE_CHOICES = [
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    title = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='full-time')
    experience = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.JSONField(default=list)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    applications = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
