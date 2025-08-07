import sqlite3
import datetime
import logging

from DB.connection_db import get_connection
from contextlib import closing



logger = logging.getLogger(__name__)
class User:
    def __init__(self, user_id, username=None, first_name=None, last_name=None):
        self.id = user_id 
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
    
    def save(self):
        try:
            with closing(get_connection()) as conn:
                cursor = conn.cursor()  

                reg_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
                cursor.execute("""
                INSERT INTO users (id, username, first_name, last_name, reg_time)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    username = excluded.username,
                    first_name = excluded.first_name,
                    last_name = excluded.last_name
                """, (self.id, self.username, self.first_name, self.last_name, reg_time))
                conn.commit()
                if cursor.rowcount > 0:
                    action = "Created" if cursor.rowcount == 1 else "Updated"
                    logger.info(f"{action} user: {self.id}")
                    return action == "Created"
                return False
            
        except sqlite3.Error as e:
            logger.error(f"Database error for user {self.id}: {e}")
            return False
        except Exception as e:
            logger.exception(f"Unexpected error for user {self.id}:")
            return False

                

