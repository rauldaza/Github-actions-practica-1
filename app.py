from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/hola', response_class=HTMLResponse)
def get_hola():
    return "<html><h1>hola Github actions, ahora con Continuous Deployment en Azure<h1></html>"