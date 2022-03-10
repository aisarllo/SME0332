# problemas sobre matrizes em python
## problema 1
la, ca, lb, cb = input().split()
la, ca, lb, cb = int(la), int(ca), int(lb), int(cb)
a = []
b = []
produto = []
elementos = []

for i in range(la):
	linhas = [float(x) for x in input().split()]
	a.append(linhas)

for i in range(lb):
	linhas = [float(x) for x in input().split()]
	b.append(linhas)

if ca != lb:
	print('Incompatíveis')
else:
	for i in range(0, la):
		produto.append([])
		for j in range(0, cb):
			produto[i].append(0)
			for k in range(0, ca):
				produto[i][j] += a[i][k]*b[k][j]
	for x in range(0, la):
		print(' '.join(('%.2f' %e for e in produto[x])))

## problema 2
l, c = input().split()
l, c = int(l), int(c)
matriz = []

for i in range(l):
	lista = []
	lista = [int(x) for x in input().split()]
	matriz.append(lista)

soma = []
ampulheta = 0
for i in range(1, l-1):
	for j in range(1, c-1):
		ampulheta = matriz[i][j] + matriz[i-1][j-1] + matriz[i-1][j] + matriz[i-1][j+1] + matriz[i+1][j-1] + matriz[i+1][j] + matriz[i+1][j+1]
		soma.append(ampulheta)

print(max(soma))

## problema 3
import numpy as np
n = int(input())
valores = input().split()
m,indice,permut,cont_maior = np.zeros((n,n)),0,1,0
linha,coluna = [],[]
for i in range(0,n):
    for j in range(0,n):
        m[i][j] = int(valores[indice])
        if int(valores[indice]) > 1:
            cont_maior += 1
        if m[i][j] == 1:
            linha.append(i)
            coluna.append(j)
        indice += 1
m = m.astype('int')
for lin in m:
    print(' '.join(map(str,lin)))
x,cont = [],0

for j in range(0,len(linha)):
    if linha[j] in x:
        cont += 1
    else:
        x.append(linha[j])
x2,cont2 = [],0

for j in range(0,len(coluna)):
    if coluna[j] in x2:
        cont2 += 1
    else:
        x2.append(coluna[j])
if cont2 > 0 or cont > 0 or cont_maior > 0:
    permut = 0
else:
    permut = 1
print('True') if permut == 1 else print('False')

## problema 5
n  = int(input())
matriz = []
soma = 0
aux = 0

for x in range(n):
	linha = [int(e) for e in input().split()]
	matriz.append(linha)

for b in range(n):
	soma += matriz[0][b]

for a in range(n):
	somalinha = 0
	for b in range(n):
		somalinha += matriz[a][b]
	if somalinha != soma:
		aux = 0
		aux += 1

for b in range(n):
	somacoluna = 0
	for a in range(n):
		somacoluna += matriz[a][b]
	if somacoluna != soma:
		aux = 0
		aux += 1

somadiagonalp = 0
somadiagonals = 0
for c in range(n):
	somadiagonalp += matriz[c][c]
	somadiagonals += matriz[n - c - 1][c]
if somadiagonalp != soma or somadiagonals != soma:
	aux = 0
	aux += 1

if aux == 1:
	print('-1')
else:
	print(soma)

## problema 7
matriz = []
encontros_m = [0,0,0,0]

for m in range(8):
    matriz.append([int(i) for i in input().split()])

for j in range(-7,15):
    encontros_u = 0
    encontros_d = 0
    for i in range(8):
        encontros_f = 0
        encontros_b = 0
        if i+j >= 0 and i+j < 8:
            encontros_d += matriz[i][i+j]
        if -i+j >= 0 and -i+j < 8:
            encontros_u += matriz[i][-i+j]
        for k in range(8):
            encontros_f += matriz[i][k]
            encontros_b += matriz[k][i]

        if encontros_m[2] < encontros_f: encontros_m[2] = encontros_f
        if encontros_m[3] < encontros_b: encontros_m[3] = encontros_b

    if encontros_m[0] < encontros_u: encontros_m[0] = encontros_u
    if encontros_m[1] < encontros_d: encontros_m[1] = encontros_d

if not (max(encontros_m) - 1):
    print('N')
else:
    print('S')

## problema 8
m = [int(i) for i in input().split()]
matriz = []

for i in range(m[0]):
    matriz.append([int(j) for j in input().split()])

for i in range(m[2]):
    a = [int(j) for j in input().split()]
    if matriz[a[0]][a[1]]: matriz[a[0]][a[1]] += -1

ganhador = 0

for i in matriz:
    ganhador += sum(i)

if not ganhador:
    print('S')
else:
    print('N')
