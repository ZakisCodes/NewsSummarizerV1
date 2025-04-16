from fastapi import FastAPI
from .routers import frontend, news_routes
from fastapi.staticfiles import StaticFiles

# Initializing the app
app =FastAPI()

app.mount("/static", StaticFiles(directory="static"),name="static")
app.include_router(frontend.router)
app.include_router(news_routes.router)
