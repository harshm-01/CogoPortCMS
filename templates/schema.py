from pydantic import BaseModel
from typing import Optional, Dict

class Config(BaseModel):
    country_code: str
    business_name: Optional[str]
    registration_numbers: Dict[str, bool]
    additional_data: Dict[str, bool]
    
    class Config:
        from_attributes = True
        