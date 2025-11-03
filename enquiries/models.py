from django.db import models

class Enquiry(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('closed', 'Closed'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=100, blank=True)
    service = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return f"{self.name} - {self.service}"

    class Meta:
        ordering = ['-date']
