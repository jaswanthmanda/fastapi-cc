"""Routers basics"""

from fastapi import APIRouter

router = APIRouter(
    prefix='/blog',
    tags=['blog'],
)

@router.get(
    '/all',
)
def index():
    return 'Returned all blogs!'
