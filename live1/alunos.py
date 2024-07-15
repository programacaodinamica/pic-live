alunos = ["Pedro", "Lara"]
# disciplinas = ["Matemática", "Português", "Ciências", "Estudos Sociais"]
notas = []
for nome in alunos:
    with open(f"notas/{nome.lower()}.csv", 'r') as arq:
        linhas = arq.readlines()
    for linha in linhas:
        partes = linha.strip().split(',')
        partes = [nome] + partes # ['Pedro'] + ['Matemática', '10']
        notas.append(tuple(partes))
print(notas)

with open("notas/resultado.csv", "w") as arq:
    arq.write("Nome, Disciplina, Nota\n")
    for linha in notas:
        arq.write(f"{linha[0]}, {linha[1]}, {linha[2]}\n")
print("FINALIZOU COM SUCESSO!")

