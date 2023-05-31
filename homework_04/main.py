"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from loguru import logger

from sqlalchemy.ext.asyncio import AsyncSession

from models import Session, Base, engine, User, Post
from jsonplaceholder_requests import fetch_posts_data, fetch_users_data

cmd = "docker compose up -d pg"


async def create_pg_docker(cmd):
    result = await asyncio.create_subprocess_shell(cmd)
    await result.communicate()
    logger.info("____pg docker rdy")


async def create_users(session: AsyncSession, users_data: list[dict]):
    for user in users_data:
        new_user = User(
            name=user["name"],
            username=user["name"],
            email=user["email"],
        )

        session.add(new_user)


async def create_posts(session: AsyncSession, posts_data: list[dict]):
    for post in posts_data:
        new_post = Post(
            title=post["title"],
            body=post["body"],
            user_id=post["userId"],
        )

        session.add(new_post)


async def async_main():
    async with Session() as session:
        await create_pg_docker(cmd)

        async with engine.begin() as connection:
            await connection.run_sync(Base.metadata.drop_all)
            await connection.run_sync(Base.metadata.create_all)

        users_data, posts_data = await asyncio.gather(
            fetch_users_data(),
            fetch_posts_data(),
        )

        await asyncio.gather(
            create_users(session=session, users_data=users_data),
            create_posts(session=session, posts_data=posts_data),
        )
        # await create_users(session=session, users_data=users_data)
        # await session.commit()
        #
        # await create_posts(session=session, posts_data=posts_data)
        await session.commit()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
