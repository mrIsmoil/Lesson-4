from django.db import models

from company.models import Kompaniya

class Elonlar(models.Model):
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
        return self.salary
