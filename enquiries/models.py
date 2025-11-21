from django.db import models

class Enquiry(models.Model):
    ENQUIRY_TYPE_CHOICES = [
        ('general', 'General Enquiry'),
        ('web_analysis', 'Web Analysis'),
    ]

    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('closed', 'Closed'),
    ]

    enquiry_type = models.CharField(max_length=20, choices=ENQUIRY_TYPE_CHOICES, default='general')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=100, blank=True)
    service = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return f"{self.name} - {self.enquiry_type}"

    class Meta:
        ordering = ['-date']
