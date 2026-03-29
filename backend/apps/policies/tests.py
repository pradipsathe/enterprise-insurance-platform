from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Policy, CustomerPolicy
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import date

User = get_user_model()

class CustomerPolicyTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="cust1", password="pass123")
        self.other_user = User.objects.create_user(username="cust2", password="pass123")
        policy = Policy.objects.create(
            title="Health Basic",
            description="Basic health coverage",
            policy_type="HEALTH",
            premium_amount=1000,
            coverage_amount=50000,
            duration_in_months=12,
            created_by=self.user
        )
        CustomerPolicy.objects.create(
            customer=self.user,
            policy=policy,
            start_date=date.today(),
            end_date=date.today(),
            status="ACTIVE"
        )
        self.token = str(RefreshToken.for_user(self.user).access_token)

    def test_authenticated_user_can_view_own_policies(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        response = self.client.get("/my-policies/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 1)

    def test_unauthenticated_user_cannot_view_policies(self):
        response = self.client.get("/my-policies/")
        self.assertEqual(response.status_code, 401)

