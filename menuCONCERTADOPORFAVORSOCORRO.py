import tkinter as tk
from tkinter import messagebox
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



class TelaTamanho(JanelaBase):
    def __init__(self, janela):
        self.var_tamanho = tk.StringVar()
        super().__init__(janela, titulo="Escolha o Tamanho", largura=700, altura=400)
        self.iniciar()
    
    def widgets(self):
        tk.Label(self.janela, text="Bem-Vindo à Pizzaria Mokele y Mbembe", width=150, height=3, font='bold').grid(row=0, column=0, sticky="W", columnspan=2)

        tk.Label(self.janela, text='Por favor, escolha o tamanho da pizza.', width=100, height=2).grid(row=1, column=0, sticky='W', columnspan=2)

        tamanhos = {
            'Broto - até 2 sabores':2,
            'Pequena - 4 fatias, até 3 sabores':3,
            'Média - 6 fatias, até 4 sabores':4,
            'Grande - 8 fatias, até 5 sabores':5,
            'Avestruz - 10 fatias, até 6 sabores':6,
        }

        for i, (nome, tamanho) in enumerate(tamanhos.items(), start=2): # Começa em dois por causa do row anterior, que era 1
            tk.Radiobutton(text=nome, variable=self.var_tamanho, value=tamanho).grid(row=i, column=0, sticky='W')


        tk.Button(self.janela, text='Confirmar', command=self.confirmarEscolha).grid(row=6, column=1, sticky='W')

    def confirmarEscolha(self):
        if not self.var_tamanho.get(): 
            messagebox.showerror('ERRO', 'É obrigatório assinalar alguma opção para prosseguir.')
            return

        print(self.var_tamanho.get())
        tamanho_da_pizza = self.var_tamanho.get()
        self.encerrar()
        janela_sabores = tk.Tk()
        janela_sabores = TelaSabores(janela_sabores, tamanho_da_pizza)
        janela_sabores.iniciar()



class TelaSabores(JanelaBase):
    def __init__(self, janela, tamanho_da_pizza):
        self.limite = int(tamanho_da_pizza)  # Converte para inteiro
        self.janela = janela
        self.totalVal = tk.IntVar(value=0)  # Inicializa o total como 0
        self.vars = {}  # Para armazenar os estados dos Checkbuttons
        self.qtdSabores_escolhidos = 0

        self.sabores = {
            'Perro Roni': 15, 'Muitsarela': 12, 'Lucas': 20, 'Micael': 18, 'Luís': 17, 
            'Yan': 16, '4 Queijos': 22, 'Calabresa': 14, 'Mokele Mbembe': 25, 'Roblox': 30
        }

        super().__init__(janela, titulo="Escolha os Sabores", largura=700, altura=400)

    def widgets(self):
        for i, (sabor, valor) in enumerate(self.sabores.items(), start=1):
            self.vars[sabor] = tk.IntVar(value=0)  # Cada Checkbutton tem sua própria variável
            tk.Checkbutton(
                self.janela, text=f"{sabor} - R${valor}", variable=self.vars[sabor],
                onvalue=1, offvalue=0, command=self.atualizar_total
            ).grid(row=i, column=0, sticky='W')

        tk.Button(self.janela, text='Confirmar', command=self.confirmarEscolha).grid(row=10, column=1, sticky='W')

    def atualizar_total(self):
        """ Atualiza o total e a quantidade de sabores escolhidos. """
        self.qtdSabores_escolhidos = sum(var.get() for var in self.vars.values())  # Conta os selecionados
        total = sum(valor for sabor, valor in self.sabores.items() if self.vars[sabor].get() == 1)  # Soma os valores
        self.totalVal.set(total)
        tk.Label(text=f'Total: R{}')

    def confirmarEscolha(self):
        if self.qtdSabores_escolhidos > self.limite:
            messagebox.showerror('ERRO', f'Você só pode escolher até no máximo {self.limite} sabores.')
            return

        print(f"Total: R${self.totalVal.get()}")
        self.encerrar()
        janela_adicionais = tk.Tk()
