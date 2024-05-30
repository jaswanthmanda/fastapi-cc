"""STATUS CODES, TAGS, SUMMARY & DESCRIPTION"""

from fastapi import FastAPI, status, Response

app = FastAPI()


@app.get(
    '/blog/{id}',
    status_code=status.HTTP_200_OK,
    tags=['blogs'],
    summary='blog api summary',
    # description='blog api description',
    response_description='This is response description in swagger',
)
def index(id: int, response: Response):
    """
    Fetch docstring as Description in swagger doc
    Get id and provide response status code acc to id value

    - **id** id parameter
    - **response** response parameter decides status code
    """
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id {id}'}
