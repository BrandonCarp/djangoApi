from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title