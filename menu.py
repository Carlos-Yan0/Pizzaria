def menuDePizzas(lista_pizzas):
    for i, (sabor, valor) in enumerate(lista_pizzas, start=1):  # Numera os itens a partir de 1
        print(f"{i}) {sabor}, R$: {valor}")  

    indice_escolhido = int(input("Escolha qualquer item digitando o número correspondente: ")) - 1  # Ajuste para índice de lista

    sabor_escolhido, valor = lista_pizzas[indice_escolhido]
    print(f"Você escolheu: {sabor_escolhido} - Preço: R$ {valor}\n")

    return valor


pizzas = {
    "Calabresa": 22,
    "Pepperoni": 25.50,
    "Quatro Queijos": 27,
    "Frango com Catupiry": 26.50
}

lista_pizzas = list(pizzas.items())  # Converte o dicionário em uma lista de tuplas (sabor, preço)

preco_total = sum(menuDePizzas(lista_pizzas) for _ in range(4))  # Executa o menu 4 vezes e usa sum() para acumular o total

print(f"Total a pagar: R$ {preco_total}")