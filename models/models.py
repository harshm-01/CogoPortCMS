from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from harshCMS.database.db import Base


class Config(Base):
    __tablename__ = "country_config_table" # Defining the table name in the database.
    country_code = Column(String, primary_key=True, index=True) # Primary key column for the country code.
    business_name = Column(String) # Column for storing the business name associated with the country.
    registration_numbers = Column(JSON) # Column for storing registration numbers, represented as JSON data.
    additional_data = Column(JSON) # Additional data column stored as JSON
