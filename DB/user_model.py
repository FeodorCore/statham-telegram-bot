import sqlite3
from datetime import datetime

class UserModel:
    def __init__(self, user_id: int, username: str | None, first_name: str | None, last_name: str | None, registr_time):
        self.user_id = user_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.registr_time = registr_time

    def save(self) -> str:
        return UserRepository.save_user(self)

    def reg_time(self) -> str:
        return UserRepository.registration_time(self.user_id)


class UserRepository:
    DB_PATH = "DB/users.db"

    @classmethod
    def initialize_db(cls):
        conn = sqlite3.connect(cls.DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                last_name TEXT,
                reg_time TEXT
            )
        """)
        conn.commit()
        conn.close()

    @classmethod
    def save_user(cls, user: UserModel) -> str:
        conn = sqlite3.connect(cls.DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT reg_time FROM users WHERE id = ?", (user.user_id,))
        existing = cursor.fetchone()

        if existing:
            cursor.execute("""
                UPDATE users 
                SET username = ?, first_name = ?, last_name = ?
                WHERE id = ?
            """, (user.username, user.first_name, user.last_name, user.user_id))
            result = "updated"
        else:
            cursor.execute("""
                INSERT INTO users (id, username, first_name, last_name, reg_time)
                VALUES (?, ?, ?, ?, ?)
            """, (user.user_id, user.username, user.first_name, user.last_name, user.registr_time))
            result = "created"

        conn.commit()
        conn.close()
        return result

