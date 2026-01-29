from http.client import HTTPException
from sqlalchemy.orm import Session
from . import repository, schemas
import os
import math
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv('BASE_URL', 'http://localhost:8000')

def create_shorten_url(db: Session, payload):
    url = repository.create_shorten_url(db, str(payload.original_url))
    
    return {
        "id": url.id,
        "original_url": url.original_url,
        "shortened_url": f"{base_url}/{url.unique_code}",
        "unique_code": url.unique_code,
        "created_at": url.created_at
    }

def get_all_history(db: Session, page: int = 1, limit: int = 10):
    page = max(1, page) 
    limit = max(1, min(100, limit))
    
    urls, total = repository.get_all_paginated(db, page, limit)
    total_pages = math.ceil(total / limit)
    
    items = []
    for url in urls:
        items.append(schemas.URLListResponse(
            id=url.id,
            original_url=url.original_url,
            unique_code=url.unique_code,
            shortened_url=f"{base_url}/{url.unique_code}",
            created_at=url.created_at
        ))
    
    return schemas.PaginatedURLResponse(
        items=items,
        total=total,
        page=page,
        limit=limit,
        total_pages=total_pages
    )

def get_original_url(db: Session, unique_code: str):
    url = repository.get_by_unique_code(db, unique_code)

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")

    return url.original_url

def delete_all_history(db: Session):
    deleted_count = repository.delete_all(db)
    return {"message": f"Deleted {deleted_count} URLs successfully"}

def delete_url_by_id(db: Session, url_id: int):
    success = repository.delete_by_id(db, url_id)
    if success:
        return {"message": f"URL with ID {url_id} deleted successfully"}
    else:
        return None