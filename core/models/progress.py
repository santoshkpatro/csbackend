import uuid
from django.db import models
from . resource import Resource
from . user import User


class Progress(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progresses')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
    last_watch_stamp = models.CharField(max_length=5, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'progresses'
        unique_together = ['user', 'resource']

    def __str__(self) -> str:
        return str(self.id)