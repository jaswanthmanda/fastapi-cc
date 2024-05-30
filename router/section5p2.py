"""API Router for post"""

from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List, Dict

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {'key': 'val'}
    image: Optional[Image] = None


@router.post('/new')
def create_a_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'data': blog,
        'version': version,
    }


# alias - Query
# router post method
@router.post('/new/{id}/comment/{comment_id}')
def create_comment(
    blog: BlogModel,
    id: int,
    comment_title: str = Query(
        None,
        title='title of the comment',
        description='Description of the comment',
        alias='commenTitle',
        deprecated=True,
    ),
    # content: str = Body('hi how are you?'), Optional
    content: str = Body(
        ...,
        min_length=10,
        max_length=20,
        regex='^[a-z\s]*$',
    ),  # ... represents as required field
    v: List[str] = Query(['1.0', '2.0', '3.0']),
    comment_id: int = Path(gt=5, le=10)
):
    return {
        'blog': blog,
        'id': id,
        'comment_id': comment_id,
        'content': content,
        'version': v,
        'comment_id': comment_id,
    }
