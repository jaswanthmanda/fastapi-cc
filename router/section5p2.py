"""API Router for post"""

from fastapi import APIRouter

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


@router.post('/new')
def create_a_blog():
    pass
