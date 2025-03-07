import tkinter as tk
from abc import ABC, abstractmethod


class BaseJanela(ABC):
    def __init__(self, titulo="Janela", largura=400, altura=300, background="white"):
        self.janela = tk.Tk()
        self.janela.title(titulo)
        self.janela.geometry(f"{largura}x{altura}")
        self.janela.config(bg=background)
        self.widgets()

    @abstractmethod
    def widgets(self):
        """Método abstrato que as subclasses devem implementar para definir widgets"""
        pass

    def iniciar(self):
        self.janela.mainloop()


class Tamanho(BaseJanela):
    def __init__(self):
        self.var_tamanhos = tk.StringVar()
        super().__init__(titulo="Escolha o Tamanho", largura=700, altura=400, background="white")

    def widgets(self):
        tk.Label(self.janela, text="Bem-Vindo à Pizzaria Mokele y Mbembe", fg="white", bg="#ff0000", width=100, height=2).grid(row=0, column=0, sticky="NSEW", columnspan=2)
        tk.Label(self.janela, text="Por favor, selecione o tamanho de sua pizza").grid(row=1, column=0, sticky="NSEW", columnspan=2)

        # Criação dos botões de tamanho de pizza
        tamanhos = ["Broto", "Média", "Grande", "Avestruz"]
        for i, tamanho in enumerate(tamanhos, start=2):
            tk.Radiobutton(self.janela, text=tamanho, variable=self.var_tamanhos, value=tamanho).grid(row=i, column=0, columnspan=2)

        # Botão de confirmação
        tk.Button(self.janela, text="Confirmar", command=self.confirmar_tamanho).grid(row=6, column=1)

    def confirmar_tamanho(self):
        tamanho_selecionado = self.var_tamanhos.get()
        if tamanho_selecionado:
            print(tamanho_selecionado)

        # Fechar a janela de tamanho e abrir a de sabores
        self.janela.withdraw()
        nova_janela = tk.Toplevel()
        Sabores(nova_janela)


class Sabores:
    def __init__(self, janela):
        self.janela_sabores = janela
        self.janela_sabores.title("Escolha os Sabores")

        tk.Label(self.janela_sabores, text="Agora vamos selecionar os sabores de sua pizza💪").grid(row=0, column=0)

        self.var_sabor1 = tk.IntVar()
        self.var_sabor2 = tk.IntVar()
        self.var_sabor3 = tk.IntVar()

        sabores = [
            ("Perro Roni", self.var_sabor1),
            ("Gatito Gatito", self.var_sabor2),
            ("Lucas Magalhães (em promoção)", self.var_sabor3),
        ]

        for i, (nome, var) in enumerate(sabores, start=1):
            tk.Checkbutton(self.janela_sabores, text=nome, variable=var).grid(row=i, column=0)

        tk.Button(self.janela_sabores, text="Confirmar", command=self.confirmar_sabores).grid(row=5, column=1)

    def confirmar_sabores(self):
        sabores_escolhidos = [
            "Perro Roni" if self.var_sabor1.get() else "",
            "Gatito Gatito" if self.var_sabor2.get() else "",
            "Lucas Magalhães" if self.var_sabor3.get() else "",
        ]
        sabores_escolhidos = [sabor for sabor in sabores_escolhidos if sabor]  # Remove strings vazias

        if sabores_escolhidos:
            print("Sabores escolhidos:", ", ".join(sabores_escolhidos))

        self.janela_sabores.withdraw()

