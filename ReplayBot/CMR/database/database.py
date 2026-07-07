import sqlite3
from CMR.models import Application

db = sqlite3.connect("cmr.db")
cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS apps (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, description TEXT, price REAL, 
        begin TEXT, end TEXT, contact TEXT
    )
""")
db.commit()

def create_application_db(name, description, price, begin, end, contact):
    try:
        app = Application(name, description, price, begin, end, contact)
        cursor.execute(
            "INSERT INTO apps (name, description, price, begin, end, contact) VALUES (?,?,?,?,?,?)",
            (name, description, price, begin, end, contact)
        )
        db.commit()
        print(f"Save ID: {cursor.lastrowid}")
        return app
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
        return None

def show_applications_db():
    cursor.execute("SELECT * FROM apps")
    rows = cursor.fetchall()
    if not rows:
        print("Нет заявок")
        return
    for row in rows:
        print(f"ID: {row[0]} | {row[1]} | {row[2]} | {row[3]} руб | {row[4]} - {row[5]} | {row[6]}")

def delete_application_db(app_id, contact):
    contact = contact.replace('@', '')
    cursor.execute("SELECT * FROM apps WHERE id = ? AND replace(contact, '@', '') = ?", (app_id, contact))
    if not cursor.fetchone():
        print(f"❌ Заявка ID {app_id} не найдена или не принадлежит вам")
        return False
    cursor.execute("DELETE FROM apps WHERE id = ?", (app_id,))
    db.commit()
    print(f"🗑️ Удалено ID: {app_id}")
    return True

def find_by_contact_db(contact):
    contact = contact.replace('@', '')
    cursor.execute("SELECT * FROM apps WHERE replace(contact, '@', '') = ?", (contact,))
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]} | {row[1]} | {row[2]} | {row[3]} руб | {row[4]} - {row[5]} | {row[6]}")
    return rows