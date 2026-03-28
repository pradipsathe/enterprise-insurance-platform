from django.db import models
import uuid
from django.conf import settings

class PolicyCategory(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(max_length=100, unique=True)

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Policy(models.Model):

    class PolicyType(models.TextChoices):
        LIFE = "LIFE", "Life"
        HEALTH = "HEALTH", "Health"
        AUTO = "AUTO", "Auto"
        HOME = "HOME", "Home"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=255)
    description = models.TextField()

    policy_type = models.CharField(
        max_length=20,
        choices=PolicyType.choices
    )

    # ✅ NEW FIELD
    category = models.ForeignKey(
        PolicyCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name="policies"
    )

    premium_amount = models.DecimalField(max_digits=10, decimal_places=2)
    coverage_amount = models.DecimalField(max_digits=12, decimal_places=2)

    duration_in_months = models.PositiveIntegerField()

    created_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="policies"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
