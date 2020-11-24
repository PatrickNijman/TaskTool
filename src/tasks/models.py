from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.TextField()
    description = models.TextField()
    id = models.UUIDField(primary_key=True)
    parent_id = models.CharField(max_length=120)
    deadline = models.DateTimeField()
    date_created = models.DateTimeField()
    workload = models.CharField(max_length=10)
    worked_time = models.TimeField()
    active = models.BooleanField(default=False)
