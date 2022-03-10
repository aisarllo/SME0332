# problemas sobre estruturas de repetição
## problema 1
n = int(input())
i = 1

while i < 11:
    print(n, '*', i, '=', n*i)
    i += 1

## problema 2
# aproximacao pi
n = int(input())
soma = 0

for k in range(0, n+1):
	soma += ((1/16**k)*
	(4/(8*k + 1) -
	2/(8*k + 4) -
	1/(8*k + 5) -
	1/(8*k + 6)))
	k += 1

print('%.48f' % soma)

## problema 3
n = int(input())
primo = 0

for i in range(1, n-1):
	i += 1
	if not n%i:
		print(i)
		primo += 1

if not primo:
	print('primo')

## problema 4
t = int(input())

for i in range(300, 1436, t):
	horas = i//60
	minutos = i%60
	print('%02d:%02d' % (horas, minutos))
	i += t

## problema 5
n = int(input())
soma = 0

for i in range(0, n-1):
	i += 1
	if not n%i:
		soma += i

if soma == n:
	print('True')
else:
	print('False')

## problema 6
n = int(input())
soma = 0
i = 0

while 0 <= i < n:
	i += 1
	soma += i/(n - (i-1))

print('%.48f' % soma)

## problema 7
n = str(input())
expoente = len(n)
soma = 0

for i in n:
	digito = int(i)
	potencia = pow(digito, expoente)
	soma += potencia

print(soma == float(n))

## problema 8
x, y, z, raio = input().split()
x, y, z, raio = int(x), int(y), int(z), int(raio)
soma = 0

for xi in range(x-raio, x+raio+1):
	for yi in range(y-raio, y+raio+1):
		for zi in range(z-raio, z+raio+1):
			if (xi - x)**2 + (yi - y)**2 + (zi - z)**2 <= raio**2 and ((xi - x)**2 + (yi - y)**2 + (zi - z)**2)%1 == 0:
				soma += 1

print(soma)

## problema 9
n = int(input())
caracteres = ''

for c in range(1, n+1):
    new = input()
    caracteres += new

nova = input()

for i in nova:
    print('{} = {}'.format(i, caracteres.count(i)))

## problema 10
nota = int(input('Informe uma nota entre 0 e 10!'))

while nota < 0 or nota > 10:
	nota = int(input('\nNota inválida, digite uma nota entre 0 e 10!'))

if 0 <= nota <= 10:
	print('\nNota válida!!!')
