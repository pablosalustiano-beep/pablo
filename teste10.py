import os
os.system("cls")


produtos = ["Arroz", "Feijão", "Café", "Açúcar"]
print(produtos)

produtos = ["Arroz", "Feijão", "Café", "Açúcar"]
produtos[1] = "Macarrão"
print(produtos)

produtos.pop(3)
print(produtos)


if "Leite" in produtos:
    produtos.remove("Leite")
else:
    print("Produto leite não encontrado.")    