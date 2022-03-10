# problemas sobre estruturas de decisão
## problema 1
import math
a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

delta = (b**2) - (4*a*c)

if delta < 0:
    print('No real roots.')
elif delta == 0:
    x1 = (-b) / (2*a)
    print('%.2f' % x1)
else:
    x1 = ((-b) - (math.sqrt(delta))) / (2*a)
    x2 = ((-b) + (math.sqrt(delta))) / (2*a)
    print('%.2f' % x1)
    print('%.2f' % x2)

## problema 2
n = int(input())

if n > 0:
	sinal = 'Positivo'
elif n == 0:
	sinal = 'Zero'
else:
	sinal = 'Negativo'

if n%2 == 0:
	paridade = 'Par'
else:
	paridade = 'Impar'

print(paridade)
print(sinal)

## problema 3
import math
x1, y1 = input().split()
x2, y2 = input().split()
x3, y3 = input().split()
x1, y1 = float(x1), float(y1)
x2, y2 = float(x2), float(y2)
x3, y3 = float(x3), float(y3)

a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
b = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
c = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)

if abs(a - b) < c < (a + b) and abs(a - c) < b < (a + c) and abs(b - c) < a < (b + c):
	print('triângulo')
	if a == b == c:
		print('equilátero')
	elif a == b or b == c or a == c:
		print('isósceles')
	else:
		print('escaleno')
else:
	print('não triângulo')

## problema 4
dia, mes = input().split('/')
dia, mes = int(dia), int(mes)

signo = ''

if mes == 1 and dia < 19:
  signo = 'Sagitário'
elif mes == 1 and dia >= 19:
  signo = 'Capricórnio'

if mes == 2 and dia < 16:
  signo = 'Capricórnio'
elif mes == 2 and dia >= 16:
  signo = 'Aquário'

if mes == 3 and dia < 12:
  signo = 'Aquário'
elif mes == 3 and dia >= 12:
  signo = 'Peixes'

if mes == 4 and dia < 19:
  signo = 'Peixes'
elif mes == 4 and dia >= 19:
  signo = 'Áries'

if mes == 5 and dia < 14:
  signo = 'Áries'
elif mes == 5 and dia >= 9:
  signo = 'Touro'

if mes == 6 and dia < 20:
  signo = 'Touro'
elif mes == 6 and dia >=20:
  signo = 'Gêmeos'

if mes == 7 and dia < 21:
  signo = 'Gêmeos'
elif mes == 7 and dia >= 21:
  signo = 'Câncer'

if mes == 8 and dia < 10:
  signo = 'Câncer'
elif mes == 8 and dia >= 10:
  signo = 'Leão'

if mes == 9 and dia < 16:
  signo = 'Leão'
elif mes == 9 and dia >= 16:
  signo = 'Virgem'

if mes == 10 and dia < 31:
  signo = 'Virgem'
elif mes == 10 and dia >= 31:
  signo = 'Libra'

if mes == 11 and dia < 23:
  signo = 'Libra'
elif mes == 11 and 23 <= dia < 30:
  signo = 'Escorpião'
elif mes == 11 and dia >= 30:
  signo = 'Serpentário'

if mes == 12 and dia < 18:
  signo = 'Serpentário'
elif mes == 12 and dia >= 18:
  signo = 'Sagitário'

print(signo)

## problema 5
mes = input()
dias = ''

if mes == 'janeiro' or mes == 'março' or mes == 'maio' or mes == 'julho' or mes == 'agosto' or mes == 'outubro' or mes == 'dezembro':
	dias = 31
elif mes == 'abril' or mes == 'junho' or mes == 'setembro' or mes == 'novembro':
	dias = 30
elif mes == 'fevereiro':
	dias = 28

print(dias)

## problema 6
ano = int(input())

if (ano%400 == 0 or (ano%4 == 0 and ano%100 != 0)):
	print('SIM')
else:
	print('NÃO')

## problema 7
linha1, coluna1 = input().split()
linha2, coluna2 = input().split()
linha1, coluna1 = int(linha1), int(coluna1)
linha2, coluna2 = int(linha2), int(coluna2)

if linha2 == linha1 and coluna2 == (coluna1 - 1):
	print('SIM')
elif linha2 == linha1 and coluna2 == (coluna1 + 1):
	print('SIM')
elif linha2 == (linha1 - 1) and coluna2 == (coluna1 - 1):
	print('SIM')
elif linha2 == (linha1 - 1) and coluna2 == coluna1:
	print('SIM')
elif linha2 == (linha1 - 1) and coluna2 == (coluna1 + 1):
	print('SIM')
elif linha2 == (linha1 + 1) and coluna2 == (coluna1 - 1):
	print('SIM')
elif linha2 == (linha1 + 1) and coluna2 == coluna1:
	print('SIM')
elif linha2 == (linha1 + 1) and coluna2 == (coluna1 + 1):
	print('SIM')
else:
	print('NÃO')

## problema 8
cv, ce, cs = input().split()
fv, fe, fs = input().split()
cv, ce, cs = int(cv), int(ce), int(cs)
fv, fe, fs = int(fv), int(fe), int(fs)

cpontos = cv*3 + ce*1
fpontos = fv*3 + fe*1

if cpontos > fpontos or (cpontos == fpontos and cs > fs):
	print('Corinthians')
elif fpontos > cpontos or (fpontos == cpontos and fs > cs):
	print('Flamengo')
elif cpontos == fpontos and cs == fs:
	print('Empate')

## problema 9
cor1 = input()
cor2 = input()

if cor1 == 'azul' and cor2 == 'vermelho':
	print('roxo')
elif cor1 == 'vermelho' and cor2 == 'azul':
	print('roxo')

if cor1 == 'vermelho' and cor2 == 'amarelo':
	print('laranja')
elif cor1 == 'amarelo' and cor2 == 'vermelho':
	print('laranja')

if cor1 == 'azul' and cor2 == 'amarelo':
	print('verde')
elif cor1 == 'amarelo' and cor2 == 'azul':
	print('verde')

if (cor1 != 'azul' and cor1 != 'vermelho' and cor1 != 'amarelo') or (cor2 != 'azul' and cor2 != 'vermelho' and cor2 != 'amarelo'):
	print('cores não primárias')

## problema 10
n = int(input())

if n < 0 or n > 36:
	print('entrada inválida')

if n == 0:
	print('verde')
elif 1 <= n <= 10 or 19 <= n <= 28:
	if n%2 == 0:
		print('preto')
	else:
		print('vermelho')
elif 11 <= n <= 18 or 29 <= n <= 36:
	if n%2 == 0:
		print('vermelho')
	else:
		print('preto')
