import sqlite3
import time

db = sqlite3.connect("/home/murat/ReplayBot/cmr.db")
cursor = db.cursor()

def get_last_id():
    cursor.execute("SELECT MAX(id) FROM apps")
    return cursor.fetchone()[0] or 0

def monitor():
    last = get_last_id()
    print(f"ID: {last}")
    while True:
        time.sleep(600)
        new = get_last_id()
        if new > last:
            print(f"Новая! ID: {new}")
            last = new

monitor()