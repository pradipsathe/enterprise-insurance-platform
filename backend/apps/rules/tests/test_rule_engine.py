from django.test import TestCase
from ..models import Rule
from ..services.rule_engine import RuleEngine

class RuleEngineTests(TestCase):
    def setUp(self):
        Rule.objects.create(
            name="Age Eligibility",
            rule_type="ELIGIBILITY",
            is_active=True,
            priority=1,
            condition_field="age",
            operator="GREATER_THAN",
            condition_value="18",
            action_type="APPROVE",
            action_value="Eligible"
        )

    def test_rule_engine_applies_rule(self):
        engine = RuleEngine("ELIGIBILITY", {"age": 20})
        result = engine.evaluate()
        self.assertIn("Eligible", [a["value"] for a in result["actions"]])
        self.assertIn("Age Eligibility", result["applied_rules"])

    def test_rule_engine_rejects_if_condition_not_met(self):
        engine = RuleEngine("ELIGIBILITY", {"age": 15})
        result = engine.evaluate()
        self.assertEqual(len(result["actions"]), 0)
