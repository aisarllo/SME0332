# problemas sobre ordenação
## problema 1
n = int(input())
lista =[]
lista_indx = []
lista_num = []
i = 0
lista  = list(input().split())
for i in range(len(lista)):
    lista[i] = int(lista[i])

lista2 = sorted(lista)

for i in range(len(lista)):
    if lista2[i] == lista[i]:
        lista_indx.append(i+1)
        lista_num.append(lista[i])

print(len(lista_indx))
for i in range(len(lista_indx)):
    print(lista_num[i],lista_indx[i])

## problema 2
lista = list(input().split())
s = 0
for i in range(len(lista)):
    lista[i] = int(lista[i])
    if lista[i] < 0:
        s += 1

if s > 0:
    print('Lista inválida!')
elif lista[0]%2 == 0:
    lista.sort()
    for i in range(len(lista)):
        lista[i] = str(lista[i])
    print(' '.join(lista))
else:
    lista.sort(reverse = True)
    for i in range(len(lista)):
        lista[i] = str(lista[i])
    print(' '.join(lista))

## problema 3
lista = [int(x) for x in input().split()]
lista.sort()

for i in range(len(lista)):
    lista[i] = str(lista[i])

print(' '.join(lista))

for i in range(len(lista)):
    lista[i] = int(lista[i])

s = 0
e = 0
lista1 =[]
lista2 = []
lista3 = []
for i in range(len(lista)):
    if lista[i] in lista1:
        lista2.append(lista[i])
    else:
        lista1.append(lista[i])

for i in range(len(lista1)):
    if lista1[i] not in lista2:
        e += 1
        print(lista1[i])
lista1 = []
for i in range(len(lista2)):
    if lista2[i] in lista1:
        lista3.append(lista2[i])
        s += 1
    else:
        lista1.append(lista2[i])

if s == 0 and e == 0:
    print(0)
elif s > 0:
    print(lista3[0])

## problema 4
n = int(input())
lista1,lista2,lista = [],[],[]
e = 0
for i in range(n):
    e = 0
    e = int(input())
    if e%2 == 0:
        lista1.append(e)
    else:
        lista2.append(e)
lista1.sort()
lista2.sort(reverse = True)

for i in range(len(lista1)):
    print(lista1[i])
for i in range(len(lista2)):
    print(lista2[i])

## problema 5
lista1 = [int(x) for x in input().split()]
lista2 = [int(x) for x in input().split()]
lsor = sorted(lista1)
lsor2 = sorted(lista2)
soma1,soma2,lista = 0,0,[]

for i in range(len(lista1)):
    if lista1[i] != lsor[i]:
        soma1 += 1
for i in range(len(lista2)):
    if lista2[i] != lsor2[i]:
        soma2 += 1
if soma1 > 0 or soma2 > 0:
    print(-1)
else:
    for i in range(len(lista1)):
        lista.append(lista1[i])
    for i in range(len(lista2)):
        lista.append(lista2[i])
    lista.sort()
    for i in range(len(lista)):
        lista[i] = str(lista[i])
    print(' '.join(lista))

## problema 6
l = list(map(float, input().split()))

for i in range(len(l)):
    j = i
    while((j > 0) and (l[j] > l[j-1])):
        tmp = l[j]
        l[j] = l[j-1]
        l[j-1] = tmp
        j = j-1
    formatted_list = ['%.2f' % x for x in l]
    print(*formatted_list)

## problema 8
n = int(input())
times = {}
l_aux = []

for i in range(n):
  jogo = eval(input())
  if jogo[0] not in times:
    times[jogo[0]] = 0
  if jogo[3] not in times:
    times[jogo[3]] = 0

  if jogo[1] > jogo[2]:
    times[jogo[0]] += 3
  elif jogo[1] < jogo[2]:
    times[jogo[3]] += 3
  elif jogo[1] == jogo[2]:
    times[jogo[3]] += 0
    times[jogo[0]] += 0

for i in times.keys():
  l_aux.append(i)

n = len(l_aux)
for i in range(n):
  for j in range(1+i,n):
    if times[l_aux[i]] > times[l_aux[j]]:
      l_aux[i], l_aux[j] = l_aux[j], l_aux[i]

for k in range(n-1,-1,-1):
  print(l_aux[k])

## problema 9
import math

def printagem(pontos, lista):
    for x in lista:
        for i in range(len(pontos)):
            if x[0] == float(pontos[i][0]) and x[1] == float(pontos[i][1]):
                print(str(pontos[i][0]) + ',' + str(pontos[i][1]))



#-----------------------------------------//--------------------------------------#

def ordenacao_quadrantes(total):
    for x in total:
        if x == max(total):
            i = total.index(x)
            lista = total[i:] + total[:i]
    return lista
#-----------------------------------------//--------------------------------------#

def quadrantes(angulos, coordenadas, centroide_x, centroide_y):
    prim_Q, seg_Q, terc_Q, quart_Q= [], [], [], []

    for i in range(len(angulos)):
        if angulos[i] < 0:
            if coordenadas[i][0] > centroide_x:
                seg_Q.append([coordenadas[i][0], coordenadas[i][1]])
            else:
                quart_Q.append([coordenadas[i][0], coordenadas[i][1]])
        if angulos[i] > 0:
            if coordenadas[i][0] > centroide_x:
                prim_Q.append([coordenadas[i][0], coordenadas[i][1]])
            else:
                terc_Q.append([coordenadas[i][0], coordenadas[i][1]])
        if angulos[i] == 0:
            if coordenadas[i][0] > centroide_x:
                prim_Q.append([coordenadas[i][0], coordenadas[i][1]])
            else:
                quart_Q.append([coordenadas[i][0], coordenadas[i][1]])



    prim_Q = sorted(prim_Q)
    seg_Q = sorted(seg_Q, reverse = True)
    terc_Q = sorted(terc_Q)
    quart_Q = sorted(quart_Q, reverse = True)
    total = prim_Q + seg_Q + terc_Q + quart_Q


    return ordenacao_quadrantes(total)
#-----------------------------------------//--------------------------------------#

def angulo(pontos_x, pontos_y, centroide_x, centroide_y):
    angulos = []
    coordenadas = []

    for i in range(len(pontos_x)):
        x = pontos_x[i] - centroide_x
        y = pontos_y[i] - centroide_y

        angulo = math.atan(y/x)
        angulo = math.degrees(angulo)
        angulos.append(angulo)
        coordenadas.append([pontos_x[i], pontos_y[i]])

    return quadrantes(angulos, coordenadas, centroide_x, centroide_y)
#-----------------------------------------//--------------------------------------#
def leitura():
    check = []
    pontos = []
    while len(check) == 0:
        coord = input()
        if coord == '*':
            check.append(1)
        else:
            coord = coord.split(',')
            pontos.append(coord)

    return pontos
#-----------------------------------------//--------------------------------------#

def centroide(pontos):
    pontos_x = []
    pontos_y = []
    for coordenada in pontos:
        pontos_x.append(float(coordenada[0]))
        pontos_y.append(float(coordenada[1]))

    centroide_x = sum(pontos_x)/len(pontos)
    centroide_y = sum(pontos_y)/len(pontos)

    return angulo(pontos_x, pontos_y, centroide_x, centroide_y)
#-----------------------------------------//--------------------------------------#

pontos = leitura()
lista = centroide(pontos)

printagem(pontos, lista)

## problema 10
def troca(paises, medalhas_Ouro, medalhas_Prata, medalhas_Bronze, j, m):
    medalhas_Ouro[j], medalhas_Ouro[m] = medalhas_Ouro[m], medalhas_Ouro[j]
    medalhas_Prata[j], medalhas_Prata[m] = medalhas_Prata[m], medalhas_Prata[j]
    medalhas_Bronze[j], medalhas_Bronze[m] = medalhas_Bronze[m], medalhas_Bronze[j]
    paises[j], paises[m] = paises[m], paises[j]

    return paises, medalhas_Ouro, medalhas_Prata, medalhas_Bronze
def classificacao(paises, med_Ouro, med_Prata, med_Bronze):
    n = len(paises)

    for i in range(n):
        m = i

        for j in range(i-1, -1, -1):
            if med_Ouro[j] < med_Ouro[m]:
                paises, med_Ouro, med_Prata, med_Bronze = troca(paises, med_Ouro, med_Prata, med_Bronze, j, m)
                m = j

            if med_Ouro[j] == med_Ouro[m]:
                if med_Prata[j] < med_Prata[m]:
                    paises, med_Ouro, med_Prata, med_Bronze = troca(paises, med_Ouro, med_Prata, med_Bronze, j, m)
                    m = j
                if med_Prata[m] == med_Prata[j]:
                    if med_Bronze[j] < med_Bronze[m]:
                        paises, med_Ouro, med_Prata, med_Bronze = troca(paises, med_Ouro, med_Prata, med_Bronze, j, m)
                        m = j
                    if med_Bronze[j] == med_Bronze[m]:
                        if paises[j] < paises[m]:
                            paises, med_Ouro, med_Prata, med_Bronze = troca(paises, med_Ouro, med_Prata, med_Bronze, j, m)
                            m = j

                    if med_Bronze[j] > med_Bronze[m]:
                        break
                if med_Prata[j] > med_Prata[m]:
                    break
            if med_Ouro[j] > med_Ouro[m]:
                break

    print('pos\tpaís\tO\tP\tB')
    for i in range(n):
        print('%d\t%s\t%d\t%d\t%d' %(i+1, paises[i], med_Ouro[i], med_Prata[i], med_Bronze[i]))

    return

#--------------------------------------------//-------------------------------
def contagem(res):
    paises = ["EUA", "CHN", "JPN", "GBR", "RUS","AUS", "FRA", "GER", "ITA", "CAN", "BRA", "CUB", "ARG"]
    medalhas_Ouro = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    medalhas_Prata = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    medalhas_Bronze = [0,0,0,0,0,0,0,0,0,0,0,0,0]

    for x in res:
        for i in range(len(paises)):
            if x[0] == paises[i]:
                if x[1] == 'ouro':
                    medalhas_Ouro[i] += 1
                if x[1] == 'prata':
                    medalhas_Prata[i] += 1
                if x[1] == 'bronze':
                    medalhas_Bronze[i] += 1

    return classificacao(paises, medalhas_Ouro, medalhas_Prata, medalhas_Bronze)

#--------------------------------------------//-------------------------------
def resultados():
    chec = []
    res = []
    while len(chec) == 0:
        resultado = input()

        if resultado == '*':
            chec.append(1)

        else:
            res.append(resultado.split())

    return contagem(res)
#--------------------------------------------//-------------------------------

resultados()
