from django.db import models

choices = (
    ('C', 'Completed'),
    ('P', 'Pending'),
)

class Task(models.Model):
    task = models.CharField(max_length=250)
    due_date = models.DateField()
    status = models.CharField(max_length=1, choices=choices)

    def __str__(self):
        return self.task
