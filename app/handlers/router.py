from fastapi import APIRouter

from app.handlers import contracts

router = APIRouter()
router.include_router(contracts.router, tags=['contracts'],
                      prefix='/contracts')
