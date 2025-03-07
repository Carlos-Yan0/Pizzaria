import classes
import os
import menu

def limpa():
    sistema = os.name
    if sistema == 'nt':  # Para Windows
        os.system('cls')


registro = classes.registro()
login = classes.login()

while True:
    esc = int(input("Digite 1 para registrar-se e 2 para logar!\n"))
    limpa()
    match esc:
        case 1:
            registro.cadastrar_usuario()
        case 2:
            while True:
                login.verificar_conta()
        case 3:
            menu.mainMenu()
        case _:
            print("Opção invalída!!")
            limpa()
