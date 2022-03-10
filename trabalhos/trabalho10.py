# problemas sobre arquivos
## problema 1
def concatena_horizontalmente(A, B, C, separador):
    listaA = open(A)
    listaB = open(B)
    listaC = open(C, 'w')
    lA = listaA.read().split('\n')
    lB = listaB.read().split('\n')
    mi = min(len(lA),len(lB))
    mm = max(len(lA),len(lB))
    for i in range(mm):
        if i < mi-1:
            listaC.write("%s%s%s\n" % (lA[i],separador, lB[i]))
        elif len(lA) > len(lB):
            listaC.write('%s\n' % lA[i])
        elif len(lB)>len(lA):
            listaC.write('%s\n' % lB[i])
    return listaC

## problema 2
def junta_listas(A, B, C):
    listaa = open(A)
    listab = open(B)
    listac = open(C, 'w')
    la = listaa.read().split('\n')
    lb = listab.read().split('\n')
    if '' in la:
        del la[-1]
    lc = []
    for i in la:
        if i in lb:
            if int(i) not in lc:
                lc.append(int(i))
    lc.sort()
    for i in lc:
        listac.write('%d' % i)
        if i != lc[-1]:
            listac.write('\n')
    return listac

## problema 3
def contagem(arquivo):
    c = 0
    arqui = open(arquivo)
    lista = ([i for i in arqui.read().split('\n')])
    if '' == lista[-1]:
        del lista[-1]

    for j in range(len(lista)):
        lista[j] = lista[j].replace(","," ")
        lista[j] = lista[j].replace("."," ")
        lista[j] = lista[j].replace("?"," ")
        lista[j] = lista[j].replace("!"," ")
        lista[j] = lista[j].replace(";"," ")
        lista[j] = lista[j].replace(":"," ")
    for i in lista:
        l = i.split()
        for j in l:
            c += 1
    return (c, len(lista))

## problema 4
def numerosbonitos(arquivo_entrada, arquivo_saida):
    Ae = open(arquivo_entrada)
    As = open(arquivo_saida, 'w')

    for i in Ae:
        for j in list(map(int, i.split())):
            if (len(str(j)) == 4) and((j % 7 == 0) or (j % 17 == 0)):
                a = ' YES'
            else:
                a = ' NO'
            As.write(str(j) + a + '\n')
    return

## problema 5
def quadro_de_medalhas(arquivo='medalhas.txt'):
    arq, ARQ = open(arquivo), open('quadro_de_medalhas.txt', 'w')
    lp = ['BRA', 'EUA', 'CHN', 'JPN', 'RUS', 'ITA', 'GER', 'GBR', 'FRA', 'CUB', 'CAN', 'AUS', 'ARG']
    l = []
    d = {}

    for i in arq:
        i = i.split()
        if i[0] not in d:
            d[i[0]] = [[0], [0], [0], [i[0]]]
            l.append(d[i[0]])
        if i[1] == 'ouro':
            d[i[0]][0][0] += 1
        elif i[1] == 'prata':
            d[i[0]][1][0] += 1
        elif i[1] == 'bronze':
            d[i[0]][2][0] += 1
    for i in lp:
        if i not in d:
            l.append([[0], [0], [0], [i]])

    l = sorted(l)[::-1]
    a = 1
    ARQ.write('pos\tpaís\tO\tP\tB\n')
    for i in l:
        s = str(a)+ '\t'+ i[3][0]+ '\t'+ str(abs(i[0][0]))+ '\t'+ str(abs(i[1][0]))+ '\t'+ str(abs(i[2][0]))+ '\n'
        ARQ.write(s)
        a += 1
    return
