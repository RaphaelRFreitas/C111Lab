#Colecoes em Python
#Colecoes sao estruturas de dados que permitem armazenar mais de um valor em uma unica variavel
#Colecoes sao divididas em 4 tipos: Listas, Tuplas, Dicionarios e Conjuntos

#Tuplas
#Tuplas sao colecoes que sao ordenadas e imutaveis
tupla = ("Goku", "Vegeta", "Trunks", "Gohan")
print(f'Tupla {tupla}')
#tupla[0] = "Kuririn" #Erro, tuplas sao imutaveis

#Listas
#Listas sao colecoes que sao ordenadas e mutaveis
lista = ["Goku", "Vegeta", "Trunks", "Gohan"]
print(f'Lista {lista}')
lista.append("Piccolo") #Create
lista[2] ="Kuririn" #Update
lista.remove("Gohan") #Delete
lista.pop(1) #Delete2
corte = lista[1:] #Slice
print(f'Lista nova {lista} e pedaco {corte}')

#Dicionarios
#Dicionarios sao colecoes que nao sao ordenadas, mutaveis e indexadas
dicionario = {"nome": "Goku", "idade": 40, "habilidade": "Kamehameha"}
print(f'Dicionario {dicionario}')

dicionario["nome"] = "Kuririn" #Update
dicionario.pop("idade") #Delete
print(f'Dicionario novo {dicionario}')

#Conjuntos
#Conjuntos sao colecoes que nao sao ordenadas e nao permitem valores duplicados
conjunto = {"Goku", "Vegeta", "Trunks", "Gohan"}
print(f'Conjunto {conjunto}')
conjunto.add("Piccolo") #Create
conjunto.remove("Gohan") #Delete
print(f'Conjunto novo {conjunto}')
