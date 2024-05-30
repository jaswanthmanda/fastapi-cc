from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()


# order will be important
# @app.get('/blog/all')
# def get_all_blogs():
#     return 'All blogs returned!'


"""QUERY PARAMETERS"""


@ app.get('/blog/all')
def get_all_blogs(
    page=1,
    page_size: Optional[int] = None
):
    return {'message': f'All {page_size} blogs on page {page}'}


"""PATH PARAMETERS"""


# PATH PARAMETERS using enum
class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f'Blog Type {type}'}


@app.get("/blog/{id}")
def index(id: int):
    return {"message": f"Blog with id {id}"}


@app.get('/blog/{id}/comments/{comment_id}')
def get_comment(
    id: int,
    comment_id: int,
    valid: bool = True,
    username: Optional[str] = None
):
    return {
        'message': f'blog_id: {id}, comment_id: {comment_id}, valid: {valid}, username: {username}'  # noqa: E501
    }
