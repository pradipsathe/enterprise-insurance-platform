from django.contrib import admin
from .models import Policy, PolicyCategory

@admin.register(PolicyCategory)
class PolicyCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


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

    list_filter = ("policy_type", "category")
    search_fields = ("title",)