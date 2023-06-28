from typing import TYPE_CHECKING

from .database import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import relationship


if TYPE_CHECKING:
    from flask_sqlalchemy.query import Query


class Post(db.Model):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(90), nullable=False)
    body = Column(Text, nullable=False, default="", server_default="")
    user_id = Column(Integer, ForeignKey("users.id"), unique=False, nullable=False)
    user = relationship(
        "User",
        back_populates="posts",
        uselist=False,
    )

    def __str__(self):
        return f"Post(id={self.id}, title={self.title}, User={self.user}"

    def __repr__(self):
        return str(self)

    if TYPE_CHECKING:
        query: Query
