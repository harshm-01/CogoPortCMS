from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .db import Base


class Config(Base):
    __tablename__ = "configurations"
    country_code = Column(String, primary_key=True, index=True)
    business_name = Column(String)
    # additional_fields = Column(JSON)