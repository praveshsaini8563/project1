from typing import List, Optional
from pydantic import BaseModel, Field


class Education(BaseModel):
    university_name: str = Field(description="Name of the university")
    degree: str = Field(description="Degree obtained")
    gpa: Optional[float] = Field(default=None, ge=0, le=10, description="GPA on a 10 point scale")


class Experience(BaseModel):
    company_name: Optional[str] = Field(default=None, description="Company name")
    years: Optional[float] = Field(default=None, ge=0, description="Years of experience")
    project_name: Optional[str] = Field(default=None, description="Main project")
    project_description: Optional[str] = Field(default=None, description="Project description")
    tech_stack: Optional[str] = Field(default=None, description="Technologies used")


class Resume(BaseModel):
    name: str = Field(description="Candidate name")
    email: str = Field(description="Email")
    phone_number: str = Field(description="Phone Number")
    education: Optional[List[Education]] = None
    experience: Optional[List[Experience]] = None
    skills: Optional[List[str]] = Field(
        default=None, description="List of technical/soft skills mentioned in resume"
    )


class JDMatchResult(BaseModel):
    match_score: float = Field(
        ge=0, le=100, description="Overall match score between resume and JD, 0-100"
    )
    matched_skills: List[str] = Field(
        default_factory=list, description="Skills from JD found in the resume"
    )
    missing_skills: List[str] = Field(
        default_factory=list, description="Skills required in JD but missing from resume"
    )
    strengths: List[str] = Field(
        default_factory=list, description="Key strengths of the candidate for this role"
    )
    gaps: List[str] = Field(
        default_factory=list, description="Key gaps/weaknesses relative to the JD"
    )
    summary: str = Field(description="Short overall assessment summary")