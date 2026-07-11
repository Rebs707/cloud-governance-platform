from fastapi import APIRouter
from app.workflows.governance_workflow import GovernanceWorkflow

router = APIRouter()

workflow = GovernanceWorkflow()


@router.get("/governance/{resource}")
def governance_check(resource: str):
    return workflow.run(resource)
