from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/ola', response_class=HTMLResponse)
def ola():
    return """
    <html>
        <head>
            <title>Olá Mundo</title>
        </head>
        <body>
            <h1>Olá Mundo!</h1>
        </body>
    </html>
    """
