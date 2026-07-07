from CMR.models import Application
from CMR.database.database import *

def create_application(name, description, price, begin, end, contact):
    try:
        app = Application(name, description, price, begin, end, contact)
        print(f"Валидация пройдена: {app}")

        result = create_application_db(name, description, price, begin, end, contact)
        return result
    except ValueError as e:
        print(f"Ошибка валидации: {e}")
        return None
    except Exception as e:
        print(f"Ошибка: {e}")
        return None


def show_applications():
    show_applications_db()


def delete_application(app_id):
    delete_application_db(app_id)


def find_by_contact(contact):
    find_by_contact_db(contact)