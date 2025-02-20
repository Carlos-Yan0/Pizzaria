pessoas = list()

class registro:
    def __init__(self):
        self.usuario = ""
        self.senha = ""
    
    def registro_usuario(self):
        self.usuario = str(input("Digite o nome de usuario: ")).strip()
        while not self.usuario:
            print("Escreva algo valído!")
            self.usuario = str(input("Digite o nome usuario: ")).strip()
        
        for pessoa in pessoas:
            if pessoa["usuario"] == self.usuario:
                print("Tente novamente com outro nome!")
                return False
        return True
        
    
    def registro_senha(self):
        self.senha = str(input("Digite uma senha(6 digitos ou mais): ")).strip()
        while len(self.senha) < 6:
            print("Sua senha deve ter no minimo 6 caracteres!")
            self.senha = str(input("Digite uma senha(6 digitos ou mais): ")).strip()
    
    def cadastrar_usuario(self):

        if self.registro_usuario():
            self.registro_senha()
            dados = {"usuario": self.usuario, "senha": self.senha}
            pessoas.append(dados)
            print("Conta criada!")



class login:
    def __init__(self):
        self.usuario = ""
        self.senha = ""
    
    def verificar_conta(self):
        self.usuario = str(input("Insira seu usuario: "))
        self.senha = str(input("Insira sua senha: "))
        for p in pessoas:
            if self.usuario == p["usuario"] and self.senha == p["senha"]:
                print(f"login bem sucedido! Bem vindo {self.usuario}")
                return False
            
        print("Algo esta errado, tente novamente!")

