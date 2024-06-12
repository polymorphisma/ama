from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request
from fastapi.security import HTTPBasic
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from dotenv import load_dotenv


load_dotenv()

app = FastAPI()
security = HTTPBasic()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("home.html", context=context)


@app.get("/test")
async def test_function(request: Request):
    return JSONResponse({"success": True, "message": "A.M.A is working"})