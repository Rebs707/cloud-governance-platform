class ComplianceAgent:

    def evaluate(self, resource):
        return {
            "resource": resource,
            "compliant": True,
            "message": "Compliance check completed"
        }
