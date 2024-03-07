from src.users.secret.vars_ambiente import username, password
from src.users.messages.responses import Messages
from src.users.methods.read.services.UserServices import UserServices


def get_user_by_id(user_id, user_name, user_password):
    if user_name == username and user_password == password:
        user_data = UserServices.get_by_id(user_id)
        if user_data:
            return Messages.get_ok_user_id(user_data)
        else:
            return Messages.get_error_user_id(user_id)
    else:
        return Messages.get_error_user_id(user_id)
