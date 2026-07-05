"""
This script is for the schemas for the API Endpoints
"""

from pydantic import BaseModel
from typing import List

class SkillRequest(BaseModel):

    skills: List[str]
    