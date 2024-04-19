from django.db import models

class Todo(models.Model):
    todo = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.todo