import uuid
from django.db import models
from .course import Course


class Module(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_free = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'modules'

    def __str__(self) -> str:
        return self.title