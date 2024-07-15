saida =[]
with open('numeros.txt','r') as arquivoEntrada, open('saida.txt','w') as arquivoSaida:
    for linha in arquivoEntrada:
        numeros = str(linha).split(' ')
        resultado = int(numeros[0])+int(numeros[1])
        saida.append(resultado)
        arquivoSaida.write(f'{str(resultado)}\n')