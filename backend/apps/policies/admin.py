from django.contrib import admin
from .models import Policy


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "policy_type",
        "premium_amount",
        "coverage_amount",
        "created_by",
        "created_at",
    )

    list_filter = ("policy_type",)
    search_fields = ("title",)