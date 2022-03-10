# problemas sobre variáveis, tipos de dados e operadores
## problema 1
num = int(input())
numinverso = int(str(num)[::-1])
print(numinverso)

## problema 2 
equacao = input()
novaequacao = equacao.upper().replace('X', 'y').replace('Y', 'x')
print(novaequacao)

## problema 3
x1, y1, z1 = input().split()
x2, y2, z2 = input().split()
x1, y1, z1 = float(x1), float(y1), float(z1)
x2, y2, z2 = float(x2), float(y2), float(z2)

xs, ys, zs = (x1 + x2, y1 + y2, z1 + z2)
d = (x1*x2 + y1*y2 + z1*z2)
xc, yc, zc = (y1*z2 - z1*y2, z1*x2 - x1*z2, x1*y2 - y1*x2)

print("%.2f" % xs, "%.2f" % ys, "%.2f" % zs)
print("%.2f" % d)
print("%.2f" % xc, "%.2f" % yc, "%.2f" % zc)

## problema 4
fahrenheit = float(input())
celsius = (5/9)*(fahrenheit - 32)
print('%.2f' % celsius)

## problema 5
t = input()

h, m, s = t.split(':')
h, m, s = float(h), float(m), float(s)

totalsegundos = (h*3600 + m*60 + s)
print(int(totalsegundos))

## problema 6
a = input()
b = input()
a, b = int(a), int(b)

funcao = 3*(a + b)*(a + b)*(a + b) + 275*b*b - 127*a - 41
print(funcao)

## problema 7
n = input()
nn = int(n + n)
nnn = int(n + n + n)
n = int(n)

soma = (n + nn + nnn)
print(soma)

## problema 8
x = int(input())

print(str(x) + '---' + str(2*x) + '---' + str(3*x) + '---' + str(4*x) + '---' + str(5*x))

## problema 9
num = int(input())

mil = num // 1000 % 10
cen = num // 100 % 10
dez = num // 10 % 10
uni = num // 1 % 10

print('O primeiro dígito é', mil)
print('O segundo dígito é', cen)
print('O terceiro dígito é', dez)
print('O quarto dígito é', uni)

## problema 10
alunos = int(input())
tangerinas = int(input())

recebido = tangerinas // alunos
cesta = tangerinas - recebido*alunos

print(recebido)
print(cesta)
