from src.users.secret.vars_ambiente import username, password
from src.users.messages.responses import Messages
from src.users.methods.read.services.UserServices import UserServices


def validate_user(user_name, user_password):
    if user_name == username and user_password == password:
        return Messages.get_ok_message(UserServices.get_all())
    else:
        return Messages.get_error_message()
