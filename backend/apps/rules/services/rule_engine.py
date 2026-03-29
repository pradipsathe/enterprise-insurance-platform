from ..models import Rule

class RuleEngine:
    def __init__(self, rule_type, input_data):
        self.rule_type = rule_type
        self.input_data = input_data
        self.applied_rules = []

    def fetch_active_rules(self):
        return Rule.objects.filter(rule_type=self.rule_type, is_active=True).order_by("priority")

    def evaluate(self):
        rules = self.fetch_active_rules()
        result = {"actions": [], "applied_rules": []}

        for rule in rules:
            field_value = self.input_data.get(rule.condition_field)
            if self._check_condition(field_value, rule.operator, rule.condition_value):
                result["actions"].append({"type": rule.action_type, "value": rule.action_value})
                result["applied_rules"].append(rule.name)

        return result

    def _check_condition(self, field_value, operator, condition_value):
        if operator == "EQUALS":
            return str(field_value) == str(condition_value)
        if operator == "GREATER_THAN":
            return float(field_value) > float(condition_value)
        if operator == "LESS_THAN":
            return float(field_value) < float(condition_value)
        if operator == "CONTAINS":
            return str(condition_value) in str(field_value)
        return False
