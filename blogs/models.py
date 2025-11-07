from django.db import models

class Blog(models.Model):
    STATUS_CHOICES = [
        ('published', 'Published'),
        ('draft', 'Draft'),
    ]

    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    content = models.TextField()
    related_to = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=100)
    publish_date = models.DateField()
    read_time = models.PositiveIntegerField(default=5, help_text="Estimated read time in minutes")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    image = models.ImageField(upload_to='blogs/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish_date']
