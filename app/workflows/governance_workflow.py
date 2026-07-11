from app.agents.compliance_agent import ComplianceAgent
from app.agents.cost_agent import CostAgent
from app.agents.security_agent import SecurityAgent
from app.agents.resource_agent import ResourceAgent


class GovernanceWorkflow:

    def run(self, resource):

        return {
            "compliance": ComplianceAgent().evaluate(resource),
            "cost": CostAgent().analyze(resource),
            "security": SecurityAgent().scan(resource),
            "resource": ResourceAgent().inventory(resource)
        }
