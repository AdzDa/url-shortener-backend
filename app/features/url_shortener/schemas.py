from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from datetime import datetime

class URLCreate(BaseModel):
    original_url: HttpUrl

class URLResponse(BaseModel): 
    id: int
    original_url: str 
    shortened_url: str
    unique_code: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class URLListResponse(BaseModel):
    id: int
    original_url: str
    unique_code: str
    shortened_url: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class PaginatedURLResponse(BaseModel):
    items: List[URLListResponse]
    total: int
    page: int
    limit: int
    total_pages: int