from rest_framework import serializers
from .models import Policy, PolicyCategory


class PolicyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyCategory
        fields = ["id", "name"]


class PolicySerializer(serializers.ModelSerializer):
    category = PolicyCategorySerializer(read_only=True)
    category_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Policy
        fields = [
            "id",
            "title",
            "description",
            "policy_type",
            "category",
            "category_id",
            "premium_amount",
            "coverage_amount",
            "duration_in_months",
            "created_by",
            "created_at",
        ]
        read_only_fields = ["id", "created_by", "created_at"]

    def create(self, validated_data):
        category_id = validated_data.pop("category_id")
        category = PolicyCategory.objects.get(id=category_id)

        validated_data["category"] = category
        validated_data["created_by"] = self.context["request"].user

        return super().create(validated_data)