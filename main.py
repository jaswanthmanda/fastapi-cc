from router import section5p1, section5p2
from fastapi import FastAPI


app = FastAPI()
app.include_router(section5p1.router)
app.include_router(section5p2.router)


@app.get('/hello')
def index():
    return 'Hello World!'
