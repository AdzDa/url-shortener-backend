from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from . import service, schemas
from app.database import get_db

router = APIRouter(
    # prefix="/url-shortener",
    # tags=["url-shortener"],
    responses={404: {"description": "URL not found"}},
)

@router.post("/", response_model=schemas.URLResponse)
def shorten_url(
    # url_request: schemas.URLRequest,
    payload: schemas.URLCreate, 
    db: Session = Depends(get_db)
):
    return service.create_shorten_url(db, payload)

@router.get("/history", response_model=schemas.PaginatedURLResponse)
def get_all_history(
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(10, ge=1, le=100, description="Number of items per page"),
    db: Session = Depends(get_db)
):
    return service.get_all_history(db, page, limit)

@router.get("/{unique_code}")
def redirect_to_original(
    unique_code: str,
    db: Session = Depends(get_db)
):
    original_url = service.get_original_url(db, unique_code)
    if original_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    
    return RedirectResponse(url=original_url, status_code=302)

@router.delete("/history")
def delete_all_history(
    db: Session = Depends(get_db)
):
    return service.delete_all_history(db)

@router.delete("/history/{url_id}")
def delete_url_by_id(
    url_id: int,
    db: Session = Depends(get_db)
):
    result = service.delete_url_by_id(db, url_id)
    if result is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return result

