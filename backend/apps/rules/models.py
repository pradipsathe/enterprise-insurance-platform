import uuid
from django.db import models

# Create your models here.
class Rule(models.Model):
    class RuleType(models.TextChoices):
        ELIGIBILITY = "ELIGIBILITY", "Eligibility"
        PREMIUM = "PREMIUM", "Premium"
        CLAIM = "CLAIM", "Claim"
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    rule_type = models.CharField(max_length=20, choices=RuleType.choices)
    is_active = models.BooleanField(default=True)
    priority = models.PositiveIntegerField(default=1)
    condition_field = models.CharField(max_length=100)
    operator = models.CharField(max_length=20)
    condition_value = models.CharField(max_length=255)
    action_type = models.CharField(max_length=50)
    action_value = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["priority"]
        
    def __str__(self):
        return f"{self.name} ({self.rule_type})"