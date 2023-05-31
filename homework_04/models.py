"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, declared_attr, relationship
import os
from sqlalchemy.orm import sessionmaker

PG_CONN_URI = (
    os.environ.get("SQLALCHEMY_PG_CONN_URI")
    or "postgresql+asyncpg://postgres:password@localhost/postgres"
)
# PG_CONN_URI = (
#     os.environ.get("SQLALCHEMY_PG_CONN_URI")
#     or "postgresql+asyncpg://username:passwd@localhost/blog"
# )


Base = declarative_base()


class User(Base):
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


class Post(Base):
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


engine = create_async_engine(
    url=PG_CONN_URI,
    echo=False,
)


Session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)
