from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, utils

def create_shorten_url(db: Session, original_url: str):
    unique_code = utils.generate_unique_code()
    
    db_url = models.URL(
        original_url=original_url, 
        unique_code=unique_code
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    
    return db_url

def get_all_paginated(db: Session, page: int = 1, limit: int = 10):
    offset = (page - 1) * limit    
    total = db.query(func.count(models.URL.id)).scalar()
    urls = db.query(models.URL).offset(offset).limit(limit).all()
    return urls, total

def delete_all(db: Session):
    deleted_count = db.query(models.URL).delete()
    db.commit()
    return deleted_count

def delete_by_id(db: Session, url_id: int):
    url = db.query(models.URL).filter(models.URL.id == url_id).first()
    if url:
        db.delete(url)
        db.commit()
        return True
    return False

def get_by_id(db: Session, url_id: int):
    return db.query(models.URL).filter(models.URL.id == url_id).first()

def get_by_unique_code(db: Session, unique_code: str):
    return db.query(models.URL).filter(models.URL.unique_code == unique_code).first()
