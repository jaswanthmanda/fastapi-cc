from fastapi import FastAPI

# init. app
myApp = FastAPI()


@myApp.get('/hello')
def index1():
    return {
        'message': 'Hello World!'
    }
