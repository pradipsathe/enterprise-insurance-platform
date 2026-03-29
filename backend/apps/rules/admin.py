from django.contrib import admin
from .models import Rule

# Register your models here.
@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ("name", "rule_type", "is_active", "priority", "created_at")
    list_filter = ("rule_type", "is_active")
    search_fields = ("name", "description", "condition_fields", "action_type")
