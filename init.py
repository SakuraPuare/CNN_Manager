import asyncio

from tortoise import Tortoise

from schemas import UserSchema


async def run():
    # 初始化数据库
    await Tortoise.init(
        db_url="mysql://root:123456@localhost:3306/cnn",
        modules={'models': ['schemas']},
    )
    # 生成schema
    await Tortoise.generate_schemas()

    # create admin account
    await UserSchema.create(username='admin', password='admin', email='admin@admin.com', is_admin=True)


if __name__ == '__main__':
    asyncio.run(run())
