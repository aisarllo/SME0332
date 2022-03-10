# problemas sobre funções em python
## problema 1
def converte(horario):
    horas = horario[0] + horario[1]
    horas = int(horas)
    if horario == '00:00':
        return '12:00 A.M'
    elif horas == 0:
        horas = horas + 12
        horas = str(horas)
        horario = horas + ':' + horario[3] + horario[4]
        return horario + ' A.M'
    elif horas < 12:
        return horario + ' A.M'
    elif 12 < horas < 22:
        horas = horas - 12
        horas = str(horas)
        horario = '0' + horas + ':' + horario[3] + horario[4]
        return horario + ' P.M'
    elif horas == 12:
        horas = str(horas)
        horario = horas + ':' + horario[3] + horario[4]
        return horario + ' P.M'
    else:
        horas = horas - 12
        horas = str(horas)
        horario = horas + ':' + horario[3] + horario[4]
        return horario + ' P.M'

while True:
    horario = input()
    if horario == '-1':
        break
    else:
        print(converte(horario))

## problema 2
def estacao_do_ano(data):
    if len(data) > 5:
        dia, mes = data.split(" de ")
        dia = int(dia)
        if mes == "janeiro":
            mes = 1
        elif mes == "fevereiro":
            mes = 2
        elif mes == "março":
            mes = 3
        elif mes == "abril":
            mes = 4
        elif mes == "maio":
            mes = 5
        elif mes == "junho":
            mes = 6
        elif mes == "julho":
            mes = 7
        elif mes == "agosto":
            mes = 8
        elif mes == "setembro":
            mes = 9
        elif mes == "outubro":
            mes = 10
        elif mes == "novembro":
            mes = 11
        elif mes == "dezembro":
            mes = 12
    else:
        dia, mes = data.split("/")
        dia, mes = int(dia), int(mes)

    if 21 <= dia <= 31 and mes == 12 or mes == 1 or mes == 2 or 1 <= dia <= 20 and mes == 3:
        return "Verão"
    elif 21 <= dia <= 31 and mes == 3 or mes == 4 or mes == 5 or 1 <= dia <= 20 and mes == 6:
        return "Outono"
    elif 21 <= dia <= 30 and mes == 6 or mes == 7 or mes == 8 or 1 <= dia <= 20 and mes == 9:
        return "Inverno"
    elif 21 <= dia <= 31 and mes == 9 or mes == 10 or mes == 11 or 1 <= dia <= 20 and mes == 12:
        return "Primavera"

    if 21 <= dia <= 31 and mes == 12 or mes == 1 or mes == 2 or 1 <= dia <= 20 and mes == 3:
        return "Verão"
    elif 21 <= dia <= 31 and mes == 3 or mes == 4 or mes == 5 or 1 <= dia <= 20 and mes == 6:
        return "Outono"
    elif 21 <= dia <= 30 and mes == 6 or mes == 7 or mes == 8 or 1 <= dia <= 20 and mes == 9:
        return "Inverno"
    elif 21 <= dia <= 31 and mes == 9 or mes == 10 or mes == 11 or 1 <= dia <= 20 and mes == 12:
        return "Primavera"

while True:
    data = input()
    if data=='-1':
        break
    else:
        print(estacao_do_ano(data))

## problema 3
#---------------------------------- TEMPLATE ----------------------------------#

def intersecta(x, y, vx, vy, cx, cy, r):
    a = (vx**2+vy**2)
    b = 2*((x-cx)*vx+(y-cy)*vy)
    c = ((x-cx)*(x-cx)+(y-cy)*(y-cy)-r*r)

    delta = b**2-4*a*c
    if (delta < 0):
        return False
    else:
        delta = delta**(1/2)
        t1 = (-b + delta)/(2*a)
        t2 = (-b - delta)/(2*a)
        if t1 > 0 or t2 > 0:
            return True
        return False

def explode(cx, cy, r):
    return [cx + r, cy, r/2, cx - r, cy, r/2, cx, cy - r, r/2, cx, cy + r, r/2]


# DAQUI EM DIANTE NÃO PRECISA ALTERAR NADA

# Quantidade de círculos iniciais
M = int(input())

# Status dos círculos:
# 2 -> círculo original,
# 1 -> círculo filho,
# 0 -> círculo inexistente

# Inicializa status
life = M * [2]

# Listas auxiliares
CX = []   # posição x dos centros dos círculos
CY = []   # posição y dos centros dos círculos
R  = []   # raio dos círculos

# Carrega as informações dos círculos iniciais
for i in range(M):
    cx, cy, r = [float(x) for x in input().split()]
    CX.append(cx)
    CY.append(cy)
    R.append(r)

# Inicializa os disparos de raios
N = int(input())
for i in range(N):
    # Carrega informações de um raio
    x, y, vx, vy = [float(k) for k in input().split()]

    # Itera sobre os círculos
    L = len(CX)
    for j in range(L):
        # se o circulo esta vivo
        if life[j] > 0:
            # se o raio intersecta o círculo
            if intersecta(x,y,vx,vy,CX[j],CY[j],R[j]):
                # se o círculo é original ele explode
                if life[j] > 1:
                    # cria novos círculos
                    children = explode(CX[j],CY[j],R[j])
                    # insere as informações dos novos círculos nas listas CX, CY e R
                    for k in range(4):
                        CX.append(children[k * 3 + 0])
                        CY.append(children[k * 3 + 1])
                        R.append(children[k * 3 + 2])
                        # os novos circulos sao marcados como filhos
                        life.append(1)
                # circulo j morre
                life[j] = 0

# Conta quantos círculos sobreviveram
count = 0
for i in life:
    if i > 0:
        count += 1

# Imprime a quantidade de círculos sobreviventes
print(count)

## problema 4
def balao(N):
    lista_S= []
    lista_F= []
    lista_F_apos = []
    lista_V= []
    lista_D= []
    for x in range(N):
        move = input()
        if move == 'S':
            soma = 10
            lista_S.append(soma)
        elif move == 'F':
            if len(lista_V) == 0:
                soma = 10
                lista_F.append(soma)
            else:
                soma = 10
                lista_F_apos.append(soma)
        elif move == 'V':
            soma = 10
            lista_V.append(soma)
        elif move == 'D':
            soma == 10
            lista_D.append(soma)

    altura = len(lista_S)*10 - (len(lista_D)*10)

    distancia = len(lista_F)*10 + len(lista_V)*10 - (len(lista_F_apos)*10)

    a = (str(altura), str(distancia))
    resp = ' '.join(a)

    return resp

N = int(input())

print(balao(N))

## problema 5
def solo(N):
    if N == 0:
        resp = 'Empate'
    elif sum(lista_deA) == sum(lista_deB):
        resp = 'Empate'
    elif sum(lista_deA) > sum(lista_deB):
        resp ='O jogador A venceu'
    else:
        resp = 'O jogador B venceu'
    return resp

d_letra = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8}
d_num = {'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8}

N = int(input())
if N == 0:
    print(solo(N))
else:
    matriz_Total_A = []
    for x in range(9):
        linha_A = input().split(' ')
        matriz_Total_A.append(linha_A)

    espaço=input()

    matriz_Total_B = []
    for x in range(9):
        linha_B = input().split(' ')
        matriz_Total_B.append(linha_B)

    espaço=input()
    if ' ' in espaço:
        espaço.remove(' ')

    lista_jogadas = []
    for x in range(N):
        jogadas = input()
        lista_jogadas.append(jogadas)

    jogadas_A = []
    for x in range(0,len(lista_jogadas),2):
        jogadas_A.append(lista_jogadas[x])

    jogadas_B = []
    for y in range(1,len(lista_jogadas),2):
        jogadas_B.append(lista_jogadas[y])

    lista_final_letra_A = []
    for z in range(0,len(jogadas_A)):
        letra_A = ((jogadas_A[z])[0])
        lista_final_letra_A.append(d_letra[letra_A])

    lista_final_num_A = []
    for z1 in range(0,len(jogadas_A)):
        num_A = ((jogadas_A[z1])[1])
        lista_final_num_A.append(d_num[num_A])

    lista_final_letra_B = []
    for w in range(0,len(jogadas_B)):
        letra_B = ((jogadas_B[w])[0])
        lista_final_letra_B.append(d_letra[letra_B])

    lista_final_num_B = []
    for w1 in range(0,len(jogadas_B)):
        num_B = ((jogadas_B[w1])[1])
        lista_final_num_B.append(d_num[num_B])

    lista_deA = []
    lista_deA.append(int(matriz_Total_B[lista_final_letra_A[0]][lista_final_num_A[0]]))
    lista_deA.append(int(matriz_Total_B[lista_final_letra_A[1]][lista_final_num_A[1]]))
    lista_deA.append(int(matriz_Total_B[lista_final_letra_A[2]][lista_final_num_A[2]]))

    lista_deB = []
    lista_deB.append(int(matriz_Total_A[lista_final_letra_B[0]][lista_final_num_B[0]]))
    lista_deB.append(int(matriz_Total_A[lista_final_letra_B[1]][lista_final_num_B[1]]))
    lista_deB.append(int(matriz_Total_A[lista_final_letra_B[2]][lista_final_num_B[2]]))

    print(solo(N))
