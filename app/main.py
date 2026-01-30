from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.features.url_shortener.controller import router as url_shortener
from app.database import create_tables
from fastapi.middleware.cors import CORSMiddleware

# Startup: Create table
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(
    title="URL Shortener API",
    description="Stage 1: Technical Assessment",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    # allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    # allow_methods=["*"], 
    allow_methods=["GET", "POST", "DELETE"], 
    allow_headers=["*"], 
)

@app.get("/")
def read_root():
    return {"message": "URL shortener service is running."}

app.include_router(
    url_shortener,
    prefix="/url-shortener",
    tags=["url-shortener"],
    responses={404: {"description": "URL not found"}}
)