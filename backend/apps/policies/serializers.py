from rest_framework import serializers
from .models import Policy, PolicyCategory, CustomerPolicy
from datetime import date, timedelta


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
    
class PurchasePolicySerializer(serializers.ModelSerializer):

    policy_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = CustomerPolicy
        fields = ["id", "policy_id", "start_date", "end_date", "status"]
        read_only_fields = ["id", "end_date", "status"]

    def validate(self, data):
        user = self.context["request"].user
        policy_id = data.get("policy_id")

        # ❌ Prevent duplicate active policy
        if CustomerPolicy.objects.filter(
            customer=user,
            policy_id=policy_id,
            status="ACTIVE"
        ).exists():
            raise serializers.ValidationError(
                "You already have an active policy."
            )

        return data

    def create(self, validated_data):
        user = self.context["request"].user
        policy_id = validated_data.pop("policy_id")

        policy = Policy.objects.get(id=policy_id)

        start_date = validated_data.get("start_date")

        # ✅ Auto calculate end_date
        end_date = start_date + timedelta(
            days=policy.duration_in_months * 30
        )

        return CustomerPolicy.objects.create(
            customer=user,
            policy=policy,
            start_date=start_date,
            end_date=end_date,
            status="ACTIVE"
        )