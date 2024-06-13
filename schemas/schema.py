from pydantic import BaseModel
from typing import Optional, Dict

class Config(BaseModel):
    country_code: str # Required: Country code of the business
    business_name: Optional[str] # Optional: Name of the business
    registration_numbers: Dict[str, bool] # Key-value pairs where keys are registration numbers (str) and values are boolean indicators representing whether it is mandatory for user to give such details or not
    additional_data: Dict[str, bool] # This Key-value pairs represent additional data to be required
    
    class Config:
        from_attributes = True
        