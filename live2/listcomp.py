nomes_arquivos = [
    "bola.png", "texto.txt", "page.pdf", "medalha.png"
]

# imagens = []
# for nome in nomes_arquivos:
#     if nome.endswith(".png"):
#         imagens.append(nome)
# list comprehension
imagens = [a.split(".")[0] for a in nomes_arquivos 
                if a.endswith(".png")] 
print(imagens)