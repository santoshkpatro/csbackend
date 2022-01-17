import shortuuid
from django.db import models
from .course import Course
from .user import User


class Order(models.Model):
    ORDER_STATUS_CHOICES = (
        ('INITIATED', 'INITIATED'),
        ('PROCESSING', 'PROCESSING'),
        ('SUCCESSFUL', 'SUCCESSFUL'),
        ('DECLINED', 'DECLINED'),
        ('CANCELLED', 'CANCELLED')
    )

    id = models.CharField(max_length=12, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='orders')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    transaction_id = models.CharField(max_length=50, blank=True, null=True)
    payment_id = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=10, default='INITIATED', choices=ORDER_STATUS_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders'

    def __str__(self) -> str:
        return str(self.id)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = shortuuid.ShortUUID().random(length=10).upper()
        return super().save(*args, **kwargs)