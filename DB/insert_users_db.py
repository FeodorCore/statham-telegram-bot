import datetime

from DB.connection_db import get_connection

import logging

def start_users(user_id, username=None, first_name=None, last_name=None) -> bool:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT reg_time FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()

    if user is None:
        reg_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        cursor.execute("""
        INSERT INTO users (id, username, first_name, last_name, reg_time)
        VALUES (?, ?, ?, ?, ?)
        """, (user_id, username, first_name, last_name, reg_time))
        
        logging.info("Созданы")
        
        conn.commit()
        conn.close()

        return False
    else:
        cursor.execute("""
        UPDATE users
        SET username = ?, first_name = ?, last_name = ?
        WHERE id = ?
        """, (username, first_name, last_name, user_id))

        logging.info("Обновлены")

        conn.commit()
        conn.close()

        return True
