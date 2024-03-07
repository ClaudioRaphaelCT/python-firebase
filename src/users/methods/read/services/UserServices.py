from src.users.database.firebaseConnection import get_docs


class UserServices:
    @classmethod
    def get_all(cls):
        database = []
        docs = get_docs()
        for doc in docs:
            doc_data = doc.to_dict()
            doc_data['id'] = doc.id
            database.append(doc_data)
        return database

    @classmethod
    def get_by_id(cls, user_id):
        docs = get_docs()
        for doc in docs:
            doc_data = doc.to_dict()
            if doc.id == user_id:
                doc_data['id'] = doc.id
                return doc_data
        return None
