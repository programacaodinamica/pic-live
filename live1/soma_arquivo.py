# Faça um programa que leia um arquivo de texto em que cada linha tem dois números separados por espaço em branco. Para cada linha, some os números e salve os resultados em um outro arquivo de texto (cada linha deve conter o resultado da soma da linha correspondente).
arquivo = open("numeros.txt", "r")
conteudo = arquivo.read()
arquivo.close()
partes = conteudo.split()
somas = []
for i in range(0, len(partes), 2):
    soma = float(partes[i]) + float(partes[i + 1])
    somas.append(str(soma) + "\n")
print(somas)

# resposta = ""
# for valor in somas:
#     resposta = resposta + f"{valor}\n"
# resposta = "\n".join(somas)
with open("resultados.txt", "w") as arq:
    # arq.write(resposta)
    arq.writelines(somas)
    