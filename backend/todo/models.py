from django.db import models
from datetime import datetime   

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    cration_date = models.DateTimeField(auto_now_add=True)
    duedate = models.DateTimeField(default=datetime.now(), blank=True)


    def _str_(self):
        return self.title