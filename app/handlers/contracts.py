from fastapi import APIRouter, Query, Depends, status
from fastapi.responses import FileResponse
from starlette.background import BackgroundTasks

from app.core.dependencies import create_contracts_service
from app.services.contracts import ContractService

router = APIRouter()

contract_service = create_contracts_service()


@router.get("/generate-contract", name="contracts:generate-contracts",
            status_code=status.HTTP_200_OK)
def generate_contract(
        background_tasks: BackgroundTasks,
        name: str = Query(None, min_length=5, max_length=10),
        company: str = Query(None, min_length=5, max_length=10),
        service: ContractService = Depends(contract_service),

):
    """
    Handles HTTP request with query params (name, company),
    validates query params and returns PDF File as a response.
    """

    file_path = service.generate_contract(name, company)
    background_tasks.add_task(service.delete_contract, file_path)
    return FileResponse(file_path)
