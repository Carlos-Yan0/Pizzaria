import tkinter as tk
from menu import Tamanho, Sabores  # Importando as classes diretamente

# Criar e iniciar a janela de tamanho
janela_escolha = tk.Tk()
janela_sabores = tk.Tk()

# Passando a janela de sabores para a classe de Tamanho
janela_escolha = Tamanho()
janela_escolha.iniciar()

# Iniciar a janela Sabores com a classe Sabores
janela_sabores = Sabores()
janela_sabores.iniciar()

