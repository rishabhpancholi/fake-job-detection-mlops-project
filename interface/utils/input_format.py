# General Imports
import re
from pydantic import BaseModel,model_validator,computed_field

class InputFormat(BaseModel):
    """Input Format Class for the app"""
    salary_range: str
    telecommuting: int
    has_company_logo: int
    has_questions: int
    employment_type: str
    required_experience: str
    required_education: str
    title: str
    location: str
    department: str
    company_profile: str
    description: str
    requirements: str
    benefits: str
    industry: str
    function: str
        
    @model_validator(mode='after')
    def clean_data(cls,values):
        try:
            if isinstance(values,str):
                    values = re.sub(r'[,.!:;]','',values)
                    values = re.sub(r'([a-z])([A-Z])',r'\1 \2',values)
                    values = re.sub(r'[()]','',values)
                    values = re.sub("\\", "\\\\",values)
                    values = re.sub("'", '"',values)
                    values = re.sub(r'[\x00-\x1F]+', ' ', regex=True)
                    values = re.sub("\n", " ",values)
                    values = re.sub("\t", " ",values)
                    values = values.lower()
                    values = re.sub(r'[^a-z\s]','',values)
            return values
        except Exception as e:
            raise ValueError(f"Error cleaning input data: {str(e)}")
    
    @computed_field
    @property
    def text(self)-> str:
        return f"{self.title} {self.location} {self.department} {self.company_profile} {self.description} {self.requirements} {self.benefits} {self.industry} {self.function}"

        