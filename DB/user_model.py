import aiosqlite
from datetime import datetime

class UserModel:
    def __init__(self, user_id: int, username: str | None, first_name: str | None, last_name: str | None, registr_time):
        self.user_id = user_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.registr_time = registr_time

    async def save(self) -> str:
        return await UserRepository.save_user(self)

class UserRepository:
    DB_PATH = "DB/users.db"

    @classmethod
    async def initialize_db(cls):
        async with aiosqlite.connect(cls.DB_PATH) as db:
            await db.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT,
                    first_name TEXT,
                    last_name TEXT,
                    reg_time TEXT
                )
            """)
            await db.commit()

    @classmethod
    async def save_user(cls, user: UserModel) -> str:
        async with aiosqlite.connect(cls.DB_PATH) as db:
            cursor = await db.execute("SELECT reg_time FROM users WHERE id = ?", (user.user_id,))
            existing = await cursor.fetchone()

            if existing:
                await db.execute("""
                    UPDATE users 
                    SET username = ?, first_name = ?, last_name = ?
                    WHERE id = ?
                """, (user.username, user.first_name, user.last_name, user.user_id))
                result = "updated"
            else:
                await db.execute("""
                    INSERT INTO users (id, username, first_name, last_name, reg_time)
                    VALUES (?, ?, ?, ?, ?)
                """, (user.user_id, user.username, user.first_name, user.last_name, user.registr_time))
                result = "created"

            await db.commit()
            return result

