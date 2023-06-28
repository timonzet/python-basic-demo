from typing import TYPE_CHECKING

from .database import db
from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import relationship


if TYPE_CHECKING:
    from flask_sqlalchemy.query import Query


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(180), unique=True)
    posts = relationship(
        "Post",
        back_populates="user",
        uselist=True,
    )

    def __str__(self):
        return f"User(id={self.id}, name={self.name}, username={self.username!r}, email={self.email}"

    def __repr__(self):
        return str(self)

    if TYPE_CHECKING:
        query: Query
