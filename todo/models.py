from django.db import models
import uuid
from datetime import datetime
from django.contrib.auth.models import User


class Todo(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    todo_text=models.CharField(max_length=300,blank=False,null=False)
    due_date=models.DateTimeField(null=True,blank=True)
    done=models.BooleanField(default=False,blank=True,null=True)
    created=models.DateTimeField(default=datetime.now,editable=False)

    def __str__(self):
        return self.todo_text

    class Meta:
        ordering=["done","-created"]
