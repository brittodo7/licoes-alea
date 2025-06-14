#questao 2
print('questao 2 ')
print('_'*25)

lista = []
qtd = int(input('quantos usuarios? '))
for i in range(qtd):
    nome = input(f'digite o nome do {i+1} usuario ')
    lista.append(nome)
for name in lista:
    print(name)
print(' '*5)

#questao 4    
print('questao 4')
print('_'*25)
nam = str(input('digite a palavra '))
for i in nam:
    print(i)
print(' '*5)

#questao 5
print('questao 5')
print('_'*25)
fra = str(input('digite o texto: '))
s = len(fra)
print(f'sua frase possui {s} caracteres')
print(' '*5)

#questao 6
print('questao 6')
print('_'*25)
frs = str(input('digite a frase '))
letra = str(input('qual letra existe '))
if letra in frs:
    print(f'existe ,{letra}, na frase')
else:
    print(f'nao existe {letra} na frase')
let = str(input("qual letra procurar "))
fl = frs.count(let)
print(f'existe {fl} {let} na frase')
print('  '*5)


#questao 7
print('questao 7')
print('_'*25)
def  calcu(ope,a,b):
    soma = a+b
    sub = a-b
    multi = a*b
    div = a/b
    if ope == '/' and div < 0:
        print('erro')
    if ope == '+':
        print(soma)
    elif ope == '-':
        print(sub)
    elif ope == '*':
        print(multi)
    elif ope == '/':
        print(div)
    else:
        print('erro')
ope = input('qual operação? ')
a = int(input('digite o 1 valor '))
b = int(input('digite o 2 valor '))
print('o resultado é ')
calcu(ope,a,b)
print(' Finalizamos S2 '*4)
