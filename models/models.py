from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from harshCMS.database.db import Base


class Config(Base):
    __tablename__ = "country_config_table"
    country_code = Column(String, primary_key=True, index=True)
    business_name = Column(String)
    registration_numbers = Column(JSON)
    additional_data = Column(JSON)
