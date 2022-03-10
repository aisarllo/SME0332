# problemas sobre listas em python
## problema 1
vetor = [float(x) for x in input().split()]
n = len(vetor)

soma = 0
for a in range(0, n):
    soma += vetor[a]
print('%.0f' % soma)

contador = 0
for a in range(0, n):
    if vetor[a] == vetor[-1]:
        contador += 1
print(contador)

maior = max(vetor)
print('%.0f' % maior)

posicao = ''
for a in range(n):
    if maior == vetor[a]:
        posicao += str(a) + ' '
print(posicao)

## problema 2
entrada = int(input())
lista = []
while entrada >= 0:
	if entrada >= 0:
		lista.append(entrada)
		entrada = int(input())
	else:
		break

n = len(lista)
cinco = 0
for i in range(0, n):
	if lista[i] > 5:
		cinco += 1
print(cinco)

somapares = 0
somaimpares = 0
for i in range(0, n):
	if lista[i] % 2:
		somapares += lista[i]
	else:
		somaimpares += lista[i]
print(somaimpares)
print(somapares)

print(n)

elementos = [str(i) for i in lista]
print(' '.join(elementos))

## problema 3
dt, m, n = input().split()
dt, m, n = float(dt), int(m), int(n)

particulas = [[float(x) for x in input().split()] for _ in range(n)]

for _ in range(m):
    for p in particulas:
        p[0] += p[3]*dt
        p[1] += p[4]*dt
        p[2] += p[5]*dt

for p in particulas:
    print('%.2f %.2f %.2f' % (p[0], p[1], p[2]))

## problema 4
vetor = [float(x) for x in input().split()]
soma = 0
multiplicacao = 1

for a in range(0, len(vetor)):
	soma += vetor[a]
	multiplicacao *= vetor[a]
	a += 1
	print('%.2f' % soma, '%.2f' % multiplicacao)

## problema 5
vet = [int(a) for a in input().split()]
pos = []
semdup = []

for i in range(0, len(vet)):
	if vet[i] >= 0:
		pos.append(vet[i])
	i += 1

for j in pos:
	if j not in semdup:
		semdup.append(j)

elementos = [str(x) for x in semdup]
print(' '.join(elementos))

## problema 6
vetor = [int(x) for x in input().split()]
lista = []
repeticoes = 0

for a in vetor:
	repeticoes = vetor.count(a)
	if repeticoes >= 2 and a not in lista:
		lista.append(a)
		lista.sort()

for b in lista:
	print(b, vetor.count(b))

## problema 8
a = int(input())
aconjunto = [int(i) for i in input().split()]
b = int(input())
bconjunto = [int(i) for i in input().split()]
lista = []


for i in range(0, len(aconjunto)):
	for j in range(0, len(bconjunto)):
		if aconjunto[i] == bconjunto[j]:
			lista.append(aconjunto[i])

if len(lista) > 0:
	elementos = [str(x) for x in lista]
	print(' '.join(elementos))
else:
	print('*')

## problema 9
times = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
resultados = []
for i in range(0, 15):
	resultados += [int(x) for x in input().split()]

oitavas = []
if resultados[0] > resultados[1]:
	oitavas.append(times[0])
elif resultados[0] < resultados[1]:
	oitavas.append(times[1])

if resultados[2] > resultados[3]:
	oitavas.append(times[2])
elif resultados[2] < resultados[3]:
	oitavas.append(times[3])

if resultados[4] > resultados[5]:
	oitavas.append(times[4])
elif resultados[4] < resultados[5]:
	oitavas.append(times[5])

if resultados[6] > resultados[7]:
	oitavas.append(times[6])
elif resultados[6] < resultados[7]:
	oitavas.append(times[7])

if resultados[8] > resultados[9]:
	oitavas.append(times[8])
elif resultados[8] < resultados[9]:
	oitavas.append(times[9])

if resultados[10] > resultados[11]:
	oitavas.append(times[10])
elif resultados[10] < resultados[11]:
	oitavas.append(times[11])

if resultados[12] > resultados[13]:
	oitavas.append(times[12])
elif resultados[12] < resultados[13]:
	oitavas.append(times[13])

if resultados[14] > resultados[15]:
	oitavas.append(times[14])
elif resultados[14] < resultados[15]:
	oitavas.append(times[15])

# oitavas

quartas = []
if resultados[16] > resultados[17]:
	quartas.append(oitavas[0])
elif resultados[16] < resultados[17]:
	quartas.append(oitavas[1])

if resultados[18] > resultados[19]:
	quartas.append(oitavas[2])
elif resultados[18] < resultados[19]:
	quartas.append(oitavas[3])

if resultados[20] > resultados[21]:
	quartas.append(oitavas[4])
elif resultados[20] < resultados[21]:
	quartas.append(oitavas[5])

if resultados[22] > resultados[23]:
	quartas.append(oitavas[6])
elif resultados[22] < resultados[23]:
	quartas.append(oitavas[7])

# quartas

semis = []
if resultados[24] > resultados[25]:
	semis.append(quartas[0])
elif resultados[24] < resultados[25]:
	semis.append(quartas[1])

if resultados[26] > resultados[27]:
	semis.append(quartas[2])
elif resultados[26] < resultados[27]:
	semis.append(quartas[3])

# semis

final = []
if resultados[28] > resultados[29]:
	final.append(semis[0])
elif resultados[28] < resultados[29]:
	final.append(semis[1])

vencedor = [str(x) for x in final]
print(''.join(vencedor))

## problema 10
txt = [0]
while txt[-1] != 'FIM':
	txt.append(input())
r = input().split('-')
txt.pop(0)
txt.remove('FIM')
nome = []

for i in range(len(txt)):
	tmp_val = 0
	txt[i] = txt[i].split()
	for j in range(len(r)):
		if txt[i].count(r[j]) > 0:
			tmp_val += 1
	nome.append([tmp_val, txt[i][0]])
nome.sort()

for i in range(len(nome)):
	print('%s\t%d' % (nome[i][1], nome[i][0]))
