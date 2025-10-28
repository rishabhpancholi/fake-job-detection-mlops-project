# General Imports 
import re
from typing import Literal,Annotated
from pydantic import BaseModel,Field

class ModelInput(BaseModel):
    """Model Input Schema"""
    salary_range: Annotated[Literal["Not Mentioned","Mentioned"],Field(description="Whether the offered salary is mentioned or not")]
    telecommuting: Annotated[Literal[0,1],Field(description="Whether the job is telecommuting or not")]
    has_company_logo: Annotated[Literal[0,1],Field(description="Whether the company has a logo or not")]
    has_questions: Annotated[Literal[0,1],Field(description="Whether the company has questions or not")]
    employment_type: Annotated[str,Field(description="The employment type of the job",examples=["Full-time","Part-time","Other"])]
    required_experience: Annotated[str,Field(description="The required experience level for the job",examples=["Internship","Mid-Senior level"])]
    required_education: Annotated[str,Field(description="The reuired education level for the job",examples=["Bachelor's Degree","Master's Degree"])]
    text: Annotated[str,Field(description="The text which includes the job title, location, department, company profile, description, requirements, benefits, industry and function")]
    


    