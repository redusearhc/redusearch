from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Redusearch")

# Montar estáticos y plantillas desde app/static y app/templates
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Pantalla principal:
     - Logo en <h1>
     - Mensaje “JUEGA A BUSCAR Y CONMIGO LO ENCONTRARÁS”
     - Formulario con botón Subir/Buscar y Hazte Premium
    """
    return templates.TemplateResponse("index.html", {"request": request})
