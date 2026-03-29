from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.admin.sites import AdminSite
from ..models import Rule
from ..admin import RuleAdmin

User = get_user_model()

class MockRequest:
    def __init__(self, user):
        self.user = user

class RuleAdminTests(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username="admin", password="adminpass", email="admin@example.com"
        )
        self.rule = Rule.objects.create(
            name="Eligibility Rule",
            description="Check age eligibility",
            rule_type="ELIGIBILITY",
            is_active=True,
            priority=1,
            condition_field="age",
            operator="GREATER_THAN",
            condition_value="18",
            action_type="APPROVE",
            action_value="Eligible"
        )
        self.site = AdminSite()
        self.admin = RuleAdmin(Rule, self.site)

    def test_rule_str_representation(self):
        self.assertEqual(str(self.rule), "Eligibility Rule (ELIGIBILITY)")

    def test_rule_appears_in_admin_list_display(self):
        request = MockRequest(self.admin_user)
        list_display = self.admin.get_list_display(request)
        self.assertIn("name", list_display)
        self.assertIn("rule_type", list_display)
        self.assertIn("priority", list_display)

    def test_rule_creation_in_admin(self):
        self.assertEqual(Rule.objects.count(), 1)
        self.assertEqual(self.rule.condition_field, "age")
        self.assertEqual(self.rule.operator, "GREATER_THAN")
