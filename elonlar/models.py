from django.db import models

from company.models import Kompaniya
from django.utils import timezone
import random
class PhoneVerification(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    verification_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=timezone.now)
    is_verified = models.BooleanField(default=False)
    expired_time = models.IntegerField(default=5)
    def generate_verification_code(self):
        self.verification_code = str(random.randint(100000, 999999))
        self.save()


class JobPost(models.Model):
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=100)
    company = models.ForeignKey(Kompaniya, on_delete=models.CASCADE, related_name='kompaniya')
    date_posted = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    job_type = models.CharField(max_length=50)


    def __str__(self):
        # Convert Decimal to string to avoid the TypeError
        return f"{self.title} - {str(self.salary)}"
