"""
This script is where we define our sql tables
"""

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    skills = Column(String, nullable=False)

    recommendations = relationship(
        "Recommendation", back_populates="user", cascade="all, delete-orphan"
    )


class Recommendation(Base):

    __tablename__ = "recommendations"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    job_role = Column(String, nullable=False)

    similarity_score = Column(Float, nullable=False)

    user = relationship("User", back_populates="recommendations")