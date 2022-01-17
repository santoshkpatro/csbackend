import uuid
from django.db import models
from .module import Module


class Resource(models.Model):
    RESOURCE_TYPE = (
        ('video', 'video'),
        ('attachment', 'attachment'),
        ('none', 'none')
    )

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='resources')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    src = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=10, default='none', choices=RESOURCE_TYPE)
    is_active = models.BooleanField(default=True)
    is_free = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'resources'

    def __str__(self) -> str:
        return self.title