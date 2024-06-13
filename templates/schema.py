from pydantic import BaseModel
from typing import Optional, Dict

class Config(BaseModel):
    country_code: str
    business_name: Optional[str]
    # additional_fields: Optional[Dict[str, str]]