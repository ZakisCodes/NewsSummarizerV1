from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request
import time
router = APIRouter()
template = Jinja2Templates(directory="templates")

@router.get('/')
def index(req: Request):
    return template.TemplateResponse(name="index.html", context={"request":req})

@router.get("/result")
def resultPage(req: Request):
    return template.TemplateResponse(name="result.html",  context={
        "request":req,
        "time": int(time.time())} #adds timestamp to bust cache
        )

