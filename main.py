from fastapi import FastAPI, Depends, HTTPException, Response, status
from typing import Optional
from templates import schema
from database import models
from database.db import engine, SessionLocal
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError

models.Base.metadata.create_all(engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def intro():
    return {'Data': {'Name': 'Harsh Maurya', 'Enrollment No': 20117056, 'University': 'IIT Roorkee'}}


@app.post('/create_configuration')
def create_config(request: schema.Config, db: Session = Depends(get_db)):
    try:
        new_config = models.Config(country_code=request.country_code, business_name=request.business_name)
        db.add(new_config)
        db.commit()
        db.refresh(new_config)
        return new_config
    except IntegrityError as e:
        db.rollback()  # Rollback the transaction
        raise HTTPException(status_code=400, detail="Country code already exists")  # Or another appropriate status code and message
    except Exception as e:
        db.rollback()  # Rollback the transaction for other exceptions
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    
@app.get('/get_all_configuration')
def all(db: Session = Depends(get_db)):
    config = db.query(models.Config).all()
    return config


@app.get('/get_configuration/{country}')
def get_config(country, db: Session = Depends(get_db)):
    config = db.query(models.Config).filter(models.Config.country_code == country).first()
    return config


@app.delete('/delete_configuration/{country}', status_code=status.HTTP_204_NO_CONTENT)
def delete_config(country,  db: Session = Depends(get_db)):
    config = db.query(models.Config).filter(models.Config.country_code == country)
    if not config.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The configuration with country code: {country} does not exist!")
    config.delete(synchronize_session=False)
    db.commit()
    return 'Deleted!'


@app.post('/update_configuration/{country}', status_code=status.HTTP_202_ACCEPTED)
def update_config(country, request: schema.Config, db: Session = Depends(get_db)):
    config = db.query(models.Config).filter(models.Config.country_code == country)
    if not config.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The configuration with country code: {country} does not exist!")
    config.update(request)
    db.commit()
    return "Updated Successfully!"