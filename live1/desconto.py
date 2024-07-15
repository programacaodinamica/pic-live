# Implemente um programa que dá um desconto de 12% sobre o preço de um item à venda, exibindo o valor final e o desconto.
preco = float(input("Digite o preço do produto: "))
taxa = float(input("Digite o percentual de desconto: "))
# preco = float(preco)
desconto = preco * taxa / 100
preco_final = preco - desconto
print(f"Preço inicial R${preco:.2f}")
# print("Desconto é: ", desconto)
print(f"Desconto de R${desconto:.2f}")
# print("Preço final é", preco_final)
print(f"Preço final R${preco_final:.2f}")

