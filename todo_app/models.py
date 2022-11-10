from django.db import models
from django.urls import reverse

class Task(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("detail_task", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title
