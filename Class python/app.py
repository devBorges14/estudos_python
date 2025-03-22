from class_user import User

email = input("Email: ")
password = input("Password: ")
name = input("Name: ")
age = input("Age: ")
gender = input("Gender: ").upper()

user_true = input("Sua senha por favor: ")
if user_true == password:
    user = User(email, password, name, age, gender)
    print(150 * "-")
    print(f"Email: {user.email}\nSenha: {user.password}\nNome: {user.name}\nIdade: {user.age}\nGenero: {user.gender}")
    #print(f"Email: {email}\nSenha: {password}\nNome: {name}\nIdade: {age}\nGenero: {gender}")
else:
    print("Senha invalida")

def conferir_se_genero_existe(gender):
    if gender != "M" and gender != "F":
        print("Genero invalido")
