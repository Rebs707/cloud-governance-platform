from app.workflows.governance_workflow import GovernanceWorkflow


def test_governance_workflow():

    result = GovernanceWorkflow().run("ec2-instance")

    assert result["compliance"]["compliant"] is True
    assert result["security"]["security_status"] == "Secure"
    assert result["resource"]["tracked"] is True
