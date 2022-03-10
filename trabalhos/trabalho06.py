# problemas sobre dicionários e tuplas
## problema 1
comando = eval(input())
agenda = {}

while comando[0] != 'Encerrar':
    if comando[0][0:7] == 'Inserir':
        if comando[1] not in agenda: agenda[comando[1]] = []
        if comando[0][7:] == 'Telefone': agenda[comando[1]].append(comando[2])
    else:
        if comando[0][7:] == 'Pessoa' and comando[1] in agenda:
            del agenda[comando[1]]
        else:
            if comando[1] in agenda and comando[2] in agenda[comando[1]]:
                agenda[comando[1]].remove(comando[2])

    comando = eval(input())

print(agenda)

## problema 2
trin_rna = input()
traducao = []

dictionary = {'UUU':'Phe','CUU':'Leu','UUA':'Leu','AAG':'Lis','UCU':'Ser','UAU':'Tyr','CAA':'Gln'}

for i in range(0,len(trin_rna),3):
    traducao.append(dictionary[trin_rna[i:i+3]])

print('-'.join(traducao))

## problema 3
biblioteca = {}
voo = ("a", "a")
origem = []
while len(voo) == 2:
	voo = eval(input())
	if len(voo) == 2:
		if origem.count(voo[0]) == 0:
			origem.append(voo[0])
		if voo[0] not in biblioteca.keys():
			biblioteca[voo[0]] = [voo[1]]
		elif biblioteca[voo[0]].count(voo[1]) == 0:
			biblioteca[voo[0]].append(voo[1])

x = len(origem)
i = 0
while i < x:
	s = len(biblioteca[origem[i]])
	j = 0
	if len(biblioteca[origem[i]]) == 0:
		del biblioteca[origem[i]]
		del origem[i]
		x -= 1
		i -= 1
	while j < s:
		if biblioteca[origem[i]][j] in biblioteca.keys():
			y = biblioteca[origem[i]][j]
			if biblioteca[y].count(origem[i]) == 1:
				biblioteca[origem[i]].remove(y)
				biblioteca[y].remove(origem[i])
				s -= 1
				j -= 1
		if len(biblioteca[origem[i]]) == 0:
			del biblioteca[origem[i]]
			del origem[i]
			x -= 1
			i -= 1
		j += 1
	i += 1


print(biblioteca)

## problema 4
numero = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
naipe = {'ouros':100, 'espadas':200, 'copas':300, 'paus':400}

jogador1 = input().split()
jogador2 = input().split()

jogadas = int(len(jogador1)/2)

vitorias = [0,0,0]

for i in range(jogadas):

    carta1 = naipe[jogador1[i*2 + 1]] + numero[jogador1[i*2]]
    carta2 = naipe[jogador2[i*2 + 1]] + numero[jogador2[i*2]]

    if carta1 > carta2: vitorias[1] += 1
    if carta1 < carta2: vitorias[2] += 1

if vitorias[1] != vitorias[2]:
    print(vitorias.index(max(vitorias)))
else:
    print('0')

## problema 5
alfanormal = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfaencript = input()
alfadescript = {}

alfadescript = dict([[alfaencript[i], alfanormal[i]] for i in range(26)])

fraseencript = input().split()

frasedescript = ''

for palavra in fraseencript:
    for letra in palavra:
        frasedescript += alfadescript.get(letra,letra)
    frasedescript += ' '

print(frasedescript)

## problema 6
texto = input().lower()

contafrase = texto.count('.') + texto.count('?') + texto.count('!')
contapalavra = {}

contagem = [0,0,contafrase]

for palavra in texto.split():
	for simbolo in palavra:
		if not simbolo.isalpha():
			palavra = palavra.strip(simbolo)

	contapalavra[palavra] = contapalavra.get(palavra,0) + 1

for i in list(contapalavra.values()):
	if i > 1: contagem[1] += 1
	contagem[0] += 1

print(' '.join([str(i) for i in contagem]))

## problema 7
n = int(input())
soma = 0
cont = 0
dic = dict(A=1, B=2, C=0, D=1, E=0, F=0, G=0, I=0, J=0, K=0, L=0, M=0, N=0, O=1, P=1, Q=1, R=1, S=0, T=0, U=0, V=0, W=0, X=0, Y=0, Z=0)

lista = []
for i in range(n):
    lista.append(input())

for i in lista:
    soma = 0
    for j in i:
        if j in dic:
            soma += int(dic[j])

    print(soma)

## problema 9
d,x = {},''
while x != 'FIM':
    a = input().split()
    if a[0] != 'FIM':
        d[a[0]] = a[1:]
    else:
        x = 'FIM'

acertos = input().split('-')
d_ac = {}
for i in d:
    ac = 0
    for j in d[i]:
        if str(j) in acertos:
            ac += 1
    d_ac[i] = ac

d_ac2 = {}
for i in sorted(d_ac):
    d_ac2[i] = d_ac[i]

for i in sorted(d_ac2, key = d_ac2.get):
    print(i,int(d_ac2[i])*'+')

## problema 10
dic = dict (I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
numero = list(input())
soma = 0

for i in range(len(numero)):
    soma += dic[numero[i]]
for i in range(len(numero)-1):
    if dic[numero[i]] < dic[numero[i+1]]:
        soma -= (dic[numero[i]]*2)

a = soma%5
if a == 0:
    print('O número é múltiplo de 5!')
else:
    print(f'O resto da divisão por 5 é igual a {a}!')
