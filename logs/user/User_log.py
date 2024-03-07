import os
import csv
import datetime
from src.users.database.createUsersDatabase import UsersDatabase as Users



# Defina o nome do arquivo e o caminho para o diretório
filename = f'usuario criados - {datetime.date.today()}.csv'
directory = 'C:/Users/crteixeira/Desktop/logs/'
filepath = os.path.join(directory, filename)

# Verifique se o diretório existe, se não, crie-o
if not os.path.exists(directory):
    os.makedirs(directory)

# Defina os campos do CSV
fields = ["username", "password", "createdAt"]

# Escreva os usuários no arquivo CSV
with open(filepath, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    for users in Users:
        writer.writerow(users)

print(f"Arquivo CSV '{filepath}' criado com sucesso.")

for users in Users:
    print(users)
