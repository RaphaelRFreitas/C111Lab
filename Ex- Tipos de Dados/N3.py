nome = input('Digite o nome: ')
media = float(input('Digite a média: '))
dicionario = {}
if media >= 60:
    situacao = 'AP'
else:
    situacao = 'RP'
dicionario['nome'] = nome
dicionario['media'] = media
dicionario['situacao'] = situacao
print(dicionario)