import Classes
import os

def limpa():
    sistema = os.name
    if sistema == 'nt':  # Para Windows
        os.system('cls')

registro = Classes.registro()
login = Classes.login()

while True:
    esc = int(input("Digite 1 para registrar-se e 2 para logar!\n"))
    limpa()
    match esc:
        case 1:
            registro.cadastrar_usuario()
        case 2:
            while True:
                login.verificar_conta()
        case _:
            print("Opção invalída!!")
            limpa()

# teste