from django.db import models
import uuid
from datetime import datetime


class Todo(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    todo_text=models.CharField(max_length=300,blank=False,null=False)
    due_date=models.DateTimeField(null=True,blank=True)
    done=models.BooleanField(default=False,blank=True,null=True)
    created=models.DateTimeField(default=datetime.now,editable=False)

    def __str__(self):
        return self.todo_text

    class Meta:
        ordering=["done","-created"]
