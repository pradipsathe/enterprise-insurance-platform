from django.db import models
import uuid
from django.conf import settings

class Policy(models.Model):
    class PolicyType(models.TextChoices):
        LIFE = "LIFE", "Life"
        HEALTH = "HEALTH", "Health"
        AUTO = "AUTO", "Auto"
        HOME = "HOME", "Home"
        
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    policy_type = models.CharField(
        max_length=20,
        choices=PolicyType.choices
    )
    
    premium_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    
    coverage_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    
    duration_in_months = models.PositiveIntegerField()
    
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="policies"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.title} - {self.policy_type}"