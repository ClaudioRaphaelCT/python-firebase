from datetime import datetime
from google.cloud.firestore_v1.base_query import FieldFilter
from src.users.messages.responses import Messages
from src.users.database.firebaseConnection import db


def check_existing_user(user_name):
    users_ref = db.collection('usuarios')
    query = users_ref.where(filter=FieldFilter('nome', '==', user_name)).limit(1).get()
    return len(query) > 0


def insert_user(user_name, user_password):
    if check_existing_user(user_name):
        return Messages.create_error_message()
    else:
        user_data = {
            "nome": user_name,
            "password": user_password,
            "createdAt": datetime.now()
        }
        users_ref = db.collection("usuarios")
        users_ref.add(user_data)
        return Messages.create_ok_message(user_name)


