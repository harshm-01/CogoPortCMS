from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from .db import Base


class Config(Base):
    __tablename__ = "configurations"
    country_code = Column(String, primary_key=True, index=True)
    business_name = Column(String)
    additional_data = Column(JSON)    