from starlette.responses import JSONResponse


class Messages:
    @classmethod
    def get_ok_message(cls, database):
        return {"message": "Acesso permitido!", "lista_usuarios": database}

    @classmethod
    def get_error_message(cls):
        return {"message": "Acesso negado", "hint": "Use usuario e senha do ADMIN"}

    @classmethod
    def get_ok_user_id(cls, user):
        return {"message": "Usuario existe na base de dados", "user": user}

    @classmethod
    def get_error_user_id(cls, user):
        return {"message": f'Usuario ID -> {user} não existe na base de dados'}

    @classmethod
    def create_ok_message(cls, username: str):
        return {"message": f'O usuário ##{username} foi cadastrado com sucesso!'}

    @classmethod
    def create_error_message(cls):
        return JSONResponse(status_code=400, content={"message": "Não foi possivel realizar o cadastro.",
                                                      "error_message": 'O usuário já consta na base de dados'})
