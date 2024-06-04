from router import section5p1, section5p2, user, article
from fastapi import FastAPI
from db import models
from db.database import engine

app = FastAPI()
app.include_router(section5p1.router)
app.include_router(section5p2.router)
app.include_router(user.router)
app.include_router(article.router)


@app.get('/hello')
def index():
    return 'Hello World!'


models.Base.metadata.create_all(engine)
