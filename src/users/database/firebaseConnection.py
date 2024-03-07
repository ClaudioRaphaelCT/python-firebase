import firebase_admin
from firebase_admin import credentials, firestore
from src.users.secret.vars_ambiente import private_key_json

cred = credentials.Certificate(private_key_json)
firebase_admin.initialize_app(cred)
db = firestore.client()


def get_docs():
    return db.collection('usuarios').get()


database = []
docs = get_docs()

for doc in docs:
    doc_data = doc.to_dict()
    doc_data['id'] = doc.id
    database.append(doc_data)
