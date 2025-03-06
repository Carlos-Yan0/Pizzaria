import tkinter as tk
from menu import Tamanho, Sabores  # Importando as classes diretamente

# Criar e iniciar a janela de tamanho
janela_escolha = tk.Tk()
janela_sabores = tk.Tk()

# Passando a janela de sabores para a classe de Tamanho
tamanho = Tamanho(janela_escolha, janela_sabores)

# Iniciar a janela Sabores com a classe Sabores
Sabores(janela_sabores)

# Esconder a janela de Sabores inicialmente
janela_sabores.withdraw()

janela_escolha.mainloop()
