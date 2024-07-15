# Faça um programa que leia um arquivo de texto em que cada linha tem dois números separados por espaço em branco. Para cada linha, some os números e salve os resultados em um outro arquivo de texto (cada linha deve conter o resultado da soma da linha correspondente).
arquivo = open("numeros.txt", "r")
linhas = arquivo.readlines()
arquivo.close()
print(linhas)
somas = []
for linha in linhas:
    partes = linha.strip().split()
    somas.append(str(int(partes[0]) + int(partes[1])) + '\n')
with open("resultados.txt", "w") as arq:
    arq.writelines(somas)
    