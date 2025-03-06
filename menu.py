import tkinter as tk

class Tamanho:
    def __init__(self, janela, janela_sabores):
        # Configurações básicas da janela
        self.janela = janela
        self.janela_sabores = janela_sabores
        self.janela.title("Registro de Usuário")
        self.janela.geometry("1280x720")
        self.janela.config(background="Light Blue")
        self.janela.columnconfigure(0, weight=1)
        self.janela.columnconfigure(1, weight=1)
        self.var_tamanhos = tk.StringVar()

        tk.Label(text='Bem-Vindo a pizzaria Mokele y Mbembe', fg='white', bg='#ff0000', width=100, height=2).grid(row=0, column=0, sticky='NSEW', columnspan=2)
        tk.Label(text='Por favor selecione o tamanho de sua pizza ').grid(row=1, column=0, sticky='NSEW', columnspan=2)

        # Criação dos botões de tamanho de pizza
        botao_tamanho1 = tk.Radiobutton(text='Broto', variable=self.var_tamanhos, value='Broto')
        botao_tamanho1.grid(row=2, column=0, columnspan=2)
        botao_tamanho2 = tk.Radiobutton(text='Média', variable=self.var_tamanhos, value='Média')
        botao_tamanho2.grid(row=3, column=0, columnspan=2)
        botao_tamanho3 = tk.Radiobutton(text='Grande', variable=self.var_tamanhos, value='Grande')
        botao_tamanho3.grid(row=4, column=0, columnspan=2)
        botao_tamanho4 = tk.Radiobutton(text='Avestruz', variable=self.var_tamanhos, value='Avestruz')
        botao_tamanho4.grid(row=5, column=0, columnspan=2)

        # Botão de confirmação
        botao_confirmar = tk.Button(text='Confirmar', command=self.confirmar_tamanho)
        botao_confirmar.grid(row=6, column=1)

    def confirmar_tamanho(self):
        tamanho_selecionado = self.var_tamanhos.get()
        if tamanho_selecionado == 'Broto':
            print("Broto")
        elif tamanho_selecionado == 'Média':
            print("Média")
        elif tamanho_selecionado == 'Grande':
            print("Grande")
        elif tamanho_selecionado == 'Avestruz':
            print("Avestruz")
        
        # Fechar as duas janelas
        self.janela.withdraw()  # Fecha a janela de Tamanho
        self.janela_sabores.deiconify()  # Mostra a janela Sabores novamente


class Sabores:
    def __init__(self, janela):
        self.janela_sabores = janela
        # Segunda janela: Seleção de sabores
        self.mensagem_sabor = tk.Label(self.janela_sabores, text='Agora vamos selecionar os sabores de sua pizza💪')
        self.mensagem_sabor.grid(row=0, column=0)

        self.var_sabor1 = tk.IntVar()
        self.var_sabor2 = tk.IntVar()
        self.var_sabor3 = tk.IntVar()

        self.botao_sabor1 = tk.Checkbutton(self.janela_sabores, text='Perro Roni', variable=self.var_sabor1)
        self.botao_sabor1.grid(row=1, column=0)
        self.botao_sabor2 = tk.Checkbutton(self.janela_sabores, text='gatito gatito', variable=self.var_sabor2)
        self.botao_sabor2.grid(row=2, column=0)
        self.botao_sabor3 = tk.Checkbutton(self.janela_sabores, text='lucas magalhaes(em promoção)', variable=self.var_sabor3)
        self.botao_sabor3.grid(row=3, column=0)

        self.botao_confirmar = tk.Button(self.janela_sabores, text='Confirmar', command=self.confirmar_sabores)
        self.botao_confirmar.grid(row=5, column=1)

    def confirmar_sabores(self):
        # Exemplo de como lidar com os sabores selecionados
        if self.var_sabor1.get():
            print("Perro Roni")
        if self.var_sabor2.get():
            print("Gatito Gatito")
        if self.var_sabor3.get():
            print("Lucas Magalhães")

        # Fechar a janela Sabores
        self.janela_sabores.withdraw()
