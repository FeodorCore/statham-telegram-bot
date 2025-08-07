import sqlite3
from threading import Lock


connection_lock = Lock()

def get_connection():
    with connection_lock:
        conn = sqlite3.connect("DB/users.db", check_same_thread=False)
        conn.execute("PRAGMA journal_mode=WAL;")
        return conn