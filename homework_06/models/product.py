from typing import TYPE_CHECKING

from .database import db
from sqlalchemy import (
    Column,
    Integer,
    String,
)


if TYPE_CHECKING:
    from flask_sqlalchemy.query import Query


class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    if TYPE_CHECKING:
        query: Query
