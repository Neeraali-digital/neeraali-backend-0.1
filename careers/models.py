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
    company = models.CharField(max_length=100, default='Neeraali Digital')
    location = models.CharField(max_length=100, default='Bengaluru (On-site)')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='full-time')
    experience = models.CharField(max_length=100)
    
    # Description fields
    job_description = models.TextField(default='')
    responsibilities = models.TextField(default='')
    requirements = models.JSONField(default=list) # Skills Required
    working_days_timings = models.CharField(max_length=200, default='')
    how_to_apply = models.TextField(default='', blank=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    applications = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

class JobApplication(models.Model):
    APPLICATION_TYPE_CHOICES = [
        ('interested', 'I am Interested'),
        ('referral', 'Refer a Friend'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('shortlisted', 'Shortlisted'),
        ('rejected', 'Rejected'),
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job_applications')
    application_type = models.CharField(max_length=20, choices=APPLICATION_TYPE_CHOICES)
    
    # Applicant Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    
    # Additional fields for referrals
    friend_first_name = models.CharField(max_length=100, blank=True, null=True)
    friend_last_name = models.CharField(max_length=100, blank=True, null=True)
    friend_email = models.EmailField(blank=True, null=True)
    friend_phone = models.CharField(max_length=20, blank=True, null=True)
    
    # Optional fields
    cover_letter = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    
    # Status and tracking
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        if self.application_type == 'referral':
            return f"{self.first_name} {self.last_name} referred {self.friend_first_name} {self.friend_last_name} for {self.job.title}"
        return f"{self.first_name} {self.last_name} applied for {self.job.title}"
    
    class Meta:
        ordering = ['-created_at']
