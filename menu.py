import tkinter as tk
from abc import ABC, abstractmethod


# Classe abstrata que define a estrutura básica de uma janela no Tkinter
class BaseJanela(ABC):
    def __init__(self, titulo="Janela", largura=400, altura=300, background="white"):
        """
        Inicializa a janela principal.
        Se esta classe for herdada, a subclasse deve implementar o método 'widgets()'.
        """
        self.janela = tk.Tk()  # Cria a janela principal
        self.janela.title(titulo)  # Define o título da janela
        self.janela.geometry(f"{largura}x{altura}")  # Define o tamanho da janela
        self.janela.config(bg=background)  # Define a cor de fundo da janela
        self.widgets()  # Chama o método para adicionar os widgets

    @abstractmethod
    def widgets(self):
        """Método abstrato que as subclasses devem implementar para definir os widgets do TkInter."""
        pass

    def iniciar(self):
        """Inicia o loop principal da interface gráfica."""
        self.janela.mainloop()

    def fechar(self):
        self.janela.destroy()


# Classe para a seleção do tamanho da pizza, herdando de BaseJanela
class Tamanho(BaseJanela):
    def __init__(self):
        """
        Inicializa a janela de escolha de tamanho da pizza.
        """
        self.var_tamanhos = tk.StringVar()  # Variável para armazenar o tamanho escolhido
        super().__init__(titulo="Escolha o Tamanho", largura=700, altura=400, background="white")  # Inicializa a janela

    def widgets(self):
        """
        Cria e posiciona os widgets na janela de seleção de tamanho.
        """
        tk.Label(
            self.janela, text="Bem-Vindo à Pizzaria Mokele y Mbembe",
            fg="white", bg="#ff0000", width=100, height=2
        ).grid(row=0, column=0, sticky="NSEW", columnspan=2)

        tk.Label(self.janela, text="Por favor, selecione o tamanho de sua pizza").grid(row=1, column=0, sticky="NSEW", columnspan=2)

        # Lista de tamanhos de pizza disponíveis
        tamanhos = ["Broto", "Média", "Grande", "Avestruz"]
        for i, tamanho in enumerate(tamanhos, start=2):
            tk.Radiobutton(self.janela, text=tamanho, variable=self.var_tamanhos, value=tamanho).grid(row=i, column=0, columnspan=2)

        # Botão para confirmar a seleção do tamanho
        tk.Button(self.janela, text="Confirmar", command=self.confirmar_tamanho).grid(row=6, column=1)

    def confirmar_tamanho(self):
        """
        Obtém o tamanho selecionado, exibe no console e abre a janela de seleção de sabores.
        """
        tamanho_selecionado = self.var_tamanhos.get()
        if tamanho_selecionado:
            print(f"Tamanho selecionado: {tamanho_selecionado}")

        # Esconde a janela de seleção de tamanho e abre a de sabores
        self.janela.withdraw()
        nova_janela = Sabores()
        nova_janela.iniciar()  # Inicia a nova janela


# Classe para a seleção dos sabores da pizza, herdando de BaseJanela
class Sabores(BaseJanela):
    def __init__(self):
        """
        Inicializa a janela de escolha dos sabores da pizza.
        """
        # Variáveis para armazenar os sabores escolhidos
        self.var_sabor1 = tk.IntVar()
        self.var_sabor2 = tk.IntVar()
        self.var_sabor3 = tk.IntVar()
        super().__init__(titulo="Escolha os Sabores", largura=700, altura=400, background="white")  # Inicializa a janela

    def widgets(self):
        """
        Cria e posiciona os widgets na janela de seleção de sabores.
        """
        tk.Label(self.janela, text="Agora vamos selecionar os sabores de sua pizza💪").grid(row=0, column=0)

        # Lista de sabores disponíveis
        sabores = [
            ("Perro Roni", self.var_sabor1),
            ("Gatito Gatito", self.var_sabor2),
            ("Lucas Magalhães (em promoção)", self.var_sabor3),
        ]

        for i, (nome, var) in enumerate(sabores, start=1):
            tk.Checkbutton(self.janela, text=nome, variable=var).grid(row=i, column=0)

        # Botão para confirmar a seleção dos sabores
        tk.Button(self.janela, text="Confirmar", command=self.confirmar_sabores).grid(row=5, column=1)

    def confirmar_sabores(self):
        """
        Obtém os sabores selecionados, exibe no console e fecha a janela de seleção de sabores.
        """
        sabores_escolhidos = [
            "Perro Roni" if self.var_sabor1.get() else "",
            "Gatito Gatito" if self.var_sabor2.get() else "",
            "Lucas Magalhães" if self.var_sabor3.get() else "",
        ]
        sabores_escolhidos = [sabor for sabor in sabores_escolhidos if sabor]  # Remove strings vazias

        if sabores_escolhidos:
            print("Sabores escolhidos:", ", ".join(sabores_escolhidos))

        # Fecha a janela após a seleção
        self.janela.destroy()
