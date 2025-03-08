import tkinter as tk
from abc import ABC, abstractmethod

class JanelaBase(ABC):
    def __init__(self, janela, titulo, altura, largura):
        self.janela = janela
        self.janela.title(titulo)  # Define o título da janela
        self.janela.geometry(f"{largura}x{altura}")  # Define o tamanho da janela
        self.widgets()

    @abstractmethod
    def widgets(self):
        pass

    def iniciar(self):
        self.janela.mainloop()

    def encerrar(self):
        self.janela.destroy()



class Tamanho(JanelaBase):
    def __init__(self, janela):
        self.var_tamanho = tk.StringVar()
        super().__init__(janela, titulo="Escolha o Tamanho", largura=700, altura=400)
        self.iniciar()
    
    def widgets(self):
        tk.Label(self.janela, text="Bem-Vindo à Pizzaria Mokele y Mbembe", width=150, height=3).grid(row=0, column=0, sticky="NSEW", columnspan=2)

        tk.Label(self.janela, text='Por favor, escolha o tamanho da pizza.', width=100, height=2).grid(row=1, column=0, sticky='EW', columnspan=2)

        tamanhos = [
            'Broto - até 2 sabores',
            'Pequena - 4 fatias, até 3 sabores',
            'Média - 6 fatias, até 4 sabores',
            'Grande - 8 fatias, até 5 sabores',
            'Avestruz - 10 fatias, até 6 sabores',
        ]

        for i, tamanho in enumerate(tamanhos, start=2): # Começa em dois por causa do row anterior, que era 1
            tk.Radiobutton(text=tamanho, variable=self.var_tamanho, value=tamanho).grid(row=i, column=0, sticky='E')


        tk.Button(self.janela, text='Confirmar', command=self.confirmarEscolha).grid(row=6, column=1, sticky='W')

    def confirmarEscolha(self):
        if not self.var_tamanho.get(): 
            tk.Label(self.janela, text='Marque alguma caixa para prosseguir').grid(row=7, column=0, sticky='NSWE', columnspan=2)
            return

        print(self.var_tamanho.get())
        self.encerrar()
        janela_sabores = tk.Tk()
        janela_sabores = Sabores(janela_sabores)
        janela_sabores.iniciar()



class Sabores(JanelaBase):
    def __init__(self, janela):
        self.janela = janela
        super().__init__(janela, titulo="Escolha os Sabores", largura=700, altura=400)

        sabores = [
            ('Perro Roni', 15), ('Muitsarela', 12), ('Lucas', 20), ('Micael', 18), ('Luís', 17), 
            ('Yan', 16), ('4 Queijos', 22), ('Calabresa', 14), ('Mokele Mbembe', 25), ('Roblox', 30)
        ]

        # Lista para armazenar as variáveis de seleção
        self.var_sabores = [tk.IntVar() for _ in sabores]

        # Variável para armazenar os valores selecionados
        self.valores_selecionados = []


    def widgets(self):
        for i, (sabor, valor) in enumerate(sabores, start=1):
            tk.Checkbutton(self.janela, text=f"{sabor} - R${valor}", variable=self.var_sabores[i-1], onvalue=valor, offvalue=0).grid(row=i, column=0, sticky='E')

    def confirmarEscolha(self):
        if not self.var_tamanho.get(): 
            tk.Label(self.janela, text='Marque alguma caixa para prosseguir').grid(row=7, column=0, sticky='NSWE', columnspan=2)
            return

        print(self.var_tamanho.get())
        self.encerrar()
        janela_adicionais = tk.Tk()
        # janela_sabores = Sabores(janela_sabores)
        # janela_sabores.iniciar()