from django.db import models


class Todo(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)
    semester = models.IntegerField()

    def __str__(self):
        return self.text

