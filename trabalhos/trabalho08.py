# problemas sobre recursão
## problema 1
import locale

def formato_real(valor):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    texto = locale.currency(soma,grouping=True,symbol=None)
    return 'R$ '+texto

x, v = input().split()
x, v = int(x),float(v)
i = x
soma = -100000
while i > -100:
    if i%2 == 0:
        soma += x/2
    else:
        soma += v/2
    i -= 100
print(formato_real(soma))

## problema 2
def soma_lista_rec(L):
    soma = 0
    for item in L:
        if not isinstance(item, list):
            soma += item
        else:
            soma += soma_lista_rec(item)
    return soma

## problema 3
def g(N):
    soma = 0
    for i in str(N):
        soma += int(i)
    if len(str(soma)) == 1:
        return soma
    else:
        return g(soma)

## problema 5
D = eval(input().strip())

def print_dict_rec(D, level=0):
    tabs = '\t'*level
    for chave in list(D.keys()):
        if not isinstance(D[chave],dict):
            print('%s%s: %s' % (tabs, chave, str(D[chave])))
        else:
            print('%s%s: {' % (tabs, chave))
            print_dict_rec(D[chave],level+1)
            print('%s}' % tabs)

print_dict_rec(D)

## problema 6
def Seguro(tabuleiro, N, linha, coluna):

    for i in range(N):
        if tabuleiro[linha][i]:
            return False

    for i in range(N):
        if tabuleiro[i][coluna]:
            return False

    for i,j in zip(range(linha,-1,-1),range(coluna,-1,-1)):
        if tabuleiro[i][j]:
            return False
    for i,j in zip(range(linha, N, 1),range(coluna, N, 1)):
        if tabuleiro[i][j]:
            return False

    for i,j in zip(range(linha,-1,-1),range(coluna, N, 1)):
        if tabuleiro[i][j]:
            return False
    for i,j in zip(range(linha, N, 1),range(coluna,-1,-1)):
        if tabuleiro[i][j]:
            return False
    return True


def Executar(tabuleiro, N, coluna, solucao = 0):

    if coluna == N:
        solucao += 1
        return solucao

    for i in range(N):
        if Seguro(tabuleiro, N, i, coluna):
            tabuleiro[i][coluna] = 1
            solucao = Executar(tabuleiro, N, coluna + 1, solucao)
            tabuleiro[i][coluna] = 0
    return solucao


def tabuleiro_rainhas(N):

    tabuleiro = []

    for i in range(N):
        tabuleiro.append([0]*N)

    return Executar(tabuleiro, N, 0)


n = int(input())

print(tabuleiro_rainhas(n))

## problema 7
def quantidade(l, c, M, pixels_nao_verificados=[], pixels_verificados=[]):
    for i in range(-1,2):
        for j in range(-1,2):
            if (l+i) in range(len(M)) and (c+j) in range(len(M[l+i])):
                if  M[l][c] == M[l+i][c+j] and \
                    [l+i,c+j] not in pixels_nao_verificados and \
                    [l+i,c+j] not in pixels_verificados:

                    pixels_nao_verificados.append([l+i,c+j])

    pixels_nao_verificados.remove([l,c])
    pixels_verificados.append([l,c])

    if len(pixels_nao_verificados):
        quantidade(pixels_nao_verificados[0][0],pixels_nao_verificados[0][1],M,pixels_nao_verificados,pixels_verificados)

    return len(pixels_verificados)

## problema 8
def Search(i,j,k,word,Used):
    Used.append([i,j])
    if k == len(word):
        return True
    else:
        if matriz[i-1][j] == word[k] and ([i-1,j] not in Used):
            if Search(i-1, j, k+1,word, Used):
                return True
        if matriz[i][j-1] == word[k] and ([i,j-1] not in Used):
            if Search(i, j-1, k+1,word, Used):
                return True
        if matriz[i][j+1] == word[k] and ([i,j+1] not in Used):
            if Search(i, j+1, k+1,word, Used):
                return True
        if matriz[i+1][j] == word[k] and ([i+1,j] not in Used):
            if Search(i+1, j, k+1,word, Used):
                return True
    Used.clear()
n, m = input().split()
n, m = int(n), int(m)
matriz = []
busca = []
Used = []
for i in range(n):
    matriz.append(input().split())
matriz.insert(0,[0]*m)
matriz.append([0]*m)
for i in range(len(matriz)):
    matriz[i].insert(0, 0)
    matriz[i].append(0)
b = int(input())
for i in range(b):
    busca.append(input())
for pal in busca:
    a = 0
    for i in range(1,n+1):
        for j in range(1, m+1):
            if matriz[i][j] == pal[0] and a == 0:
                if Search(i, j, 1,pal, Used):
                    print('Sim')
                    a = 1
    if a == 0:
        print('Não')
    Used.clear()

## problema 9
I = int(input())

def neyzinho(indice):


    if indice <= 0:
        return 'SEM RESPOSTA'

    else:
        if indice == 1:
            return 3
        else:
            if not indice%2:
                return 4 + neyzinho(indice-1)
            if indice%2:
                return 1 + neyzinho(indice-1)

print(neyzinho(I))

## problema 10
L, C = (int(x) for x in input().split())

tabela = [[int(x) for x in input().split()] for _ in range(L)]

D = int(input())

from copy import deepcopy


def contar1(tabela):
    contagem = 0
    for linha in tabela:
        contagem += linha.count(1)
    return contagem
def EliminarTab(tab, elim):
    tabcop = deepcopy(tab)
    if len(tab)%2 == 0:
        if elim == 0 or contar1(tabcop) == 0:
            return (tabcop, elim, contar1(tabcop))
        elif elim > 0:
            for linha in tabcop:
                for elemento in linha:
                    if elemento == 1:
                        linha[linha.index(elemento)] = 0
                        elimNova = elim - 1
                        break
                else:
                    continue
                break
            return EliminarTab(tabcop, elimNova)
    elif len(tab)%2 != 0:
        if elim == 0 or contar1(tabcop) == 0:
            return (tabcop, elim, contar1(tabcop))
        elif elim > 0:
            for coluna in range(len(tabcop[0])):
                for linha in range(len(tabcop)):
                    if tabcop[linha][coluna] == 1:
                        tabcop[linha][coluna] = 0
                        elimNova = elim - 1
                        break
                else:
                    continue
                break
            return EliminarTab(tabcop, elimNova)

tabelaNova, elimRestantes, celRestantes = EliminarTab(tabela, D)

for i in tabelaNova:
    for j in range(len(i)):
        i[j] = str(i[j])
    print(' '.join(i))

print(elimRestantes, celRestantes)
