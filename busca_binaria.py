#2010552 - Eduardo Max dos Reis Silva

def buscaBinaria(lista, chave):
    pos_ini = 0
    pos_fim = len(lista) - 1

    while pos_ini <= pos_fim:
        print('\nInício de busca =', pos_ini, 'Final de busca =', pos_fim) 
        pos_meio = (pos_ini + pos_fim) // 2

        if lista[pos_meio] == chave:
            return pos_meio
        if lista[pos_meio] > chave:
            pos_fim = pos_meio - 1
        else:
            pos_ini = pos_meio + 1

    return -1

def buscaSequencial(lista, chave):
    for (indice, numero) in enumerate(lista):
        if numero == chave:
            return indice
    return -1

lista = [20, 5, 15, 24, 67, 45, 1, 76, 21, 11]
print(lista,'\n')
chave = int(input('Qual o valor a se buscar na lista?: '))

binaria = buscaBinaria(lista, chave)
sequencial = buscaSequencial (lista, chave)

if binaria or sequencial != -1:
    print('\nUtilizando Busca Binária - Posição da chave', chave, 'na lista:', binaria)
    print('\nUtilizando Busca Sequencial - Posição da chave', chave, 'na lista:', sequencial)
else:
    print("\nA chave", chave, "não se encontra na lista")




