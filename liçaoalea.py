# licoes-alea
valores = list()
for valor in range (0, 5):
    valores.append(int(input('Digite o valor: ')))

valores.sort()
maior = valores[4]
print(f'encontrei o maior valor {maior}, na posiçao 5')
valores.sort(reverse=True)
menor = valores [0]
print(f'encontrei o menor valor {menor}, na posiçao 0')


valor = list()
v = int(input('quantos itens voce quer na lista?'))
for _ in range (0,v):
    i = int(input('Digite o valor: '))
    if i not in valor:
        valor.append(i)
    else:
        continue
valor.sort()
print (valor)


lista = list()
for i in range(5):
    n = int(input('digite o valor: '))
    if i == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(lista)


lista = list()
v = int(input('quantos itens voce quer na lista?'))
for i in range (0,v):
    lista.append(int(input('Digite o valor: ')))

j = len(lista)
print(f'o tamanho da lista é {j}')

dlista = lista.sort(reverse=True)
print(lista.sort(reverse=True), dlista)
print(lista)

if 5 in lista:
    print('o valor 5 aparece na lista')


lista_c = []
lista_p = []
lista_i = []

v = int(input('quantos itens voce quer na lista?'))
for i in range (0,v):
    n = int(input('qual o valor '))
    lista_c.append(n)
    if n % 2 == 0:
        lista_p.append(n)
    else:
        lista_i.append(n)
print(lista_c,lista_p,lista_i)


exp = input('digite a expressão')
expre = []
for letra in exp:
    if letra == '(':
        expre.append('(')
    elif letra == ')':
        if len(expre) > 0:
            expre.pop()
        else:
            expre.append(')')
            break
if len(expre) == 0:
    print('deu certo')
elif len(expre) != 0:
    print('deu erro')


import random
nomes = list(['JOTA','Bernardo','Guilherme','Arthur','AUBREY','Miranda','Maria Luiza','Nicolas','PINTO','Carlão','fusco','yasmin','SOPHIA','bryeto','flora','math','GIULIA','ale','Jackson','victoria','DIOGO','Emilly','Heitor','murilo','COELHO','Britto','Isabelly','Layla','GORDINHO','Medina','Helo','Vietri']) #lista de nomes

for i in range(8): #repete 8 grupos
    a = random.sample(nomes, k=4) #escolhe nomes randoms 'K' tamanho do grupo
    for nome in a:
        nomes.remove(nome) #tira os nomes que ja foram da lista
    print(f'o grupo {i+1} ficou :{a}') #mostra a lista

produtos = ['Computador', 'Mouse', 'Teclado']
for indice, produto in enumerate(produtos):
    print(f'produto {indice+1} : produto {produto}')
    
def media(a):
    soma = sum(a)
    qtd = len(a)
    media = soma/qtd
    print(f'a media é {media}')
    return media
notas_alunos = [8, 7, 5, 9, 6]
media(notas_alunos)

salarios = [3000, 5000, 7000]
for salario in salarios:
    print(f'o salario ficou {(salario * 0.10) + salario}')
    
alturas_alunos = [160, 175, 150, 180]
for indice, altura in enumerate(alturas_alunos):
    print(f'aluno {indice+1} : altura {altura}')

personagens = [100, 0, 50, 75]
for ind, vida in enumerate(personagens):
    print(f'personagem {ind+1} ',end='')
    if vida > 0:print('vivo')
    else:print('morto')
    
def conversao(graus):
    fahre = list()
    for grau in graus:
        f = (grau * (9/5)) + 32
        fahre.append(f)
    print(fahre)
    return fahre
celsius = [20, 25, 30]
conversao(celsius)

def avaliacao(notas):
    for ind, nota in enumerate(notas):
        if nota >= 6:
            a = True
        else:
            a = False
        print(f'aluno {ind+1} : aprovação {a}')
alunos = [7, 5, 8, 4, 6]
avaliacao(alunos)
print('ola sistema de restaurante')
mesas = [2, 4, 6]
print('mesas disponiveis:')
for mesa in mesas:
    print(f'mesa N-{mesa}, 4 lugares')
esc = int(input('qual mesa voce quer? '))
if esc not in mesas:
    print('MESA NAO DISPONIVEL')
else:
    mesas.remove(esc)
    print(f'ok mesa N-{esc} reservada ')
    print(f'mesas disponiveis: {mesas}')
   
tarefas = ['Estudar Python', 'Fazer compras', 'Enviar e#-mails']
for ind, tarefa in enumerate(tarefas):
    print(f'tarefa {ind+1} : a fzer {tarefa}')
    
def total (lista):
    soma = sum(lista)
    print(f'o total ficou {soma}')
    return soma
precos = [10.5, 5.2, 8.0, 12.99]
total(precos)
def contar (lista):
    for ind, letra in enumerate(lista):
        a = len(letra)
        print(f'a palavra {ind+1} tem {a} letras')
palavras = ['python', 'exemplo', 'programacao']
contar(palavras)

def converter(celcius):
    for ind, valor in enumerate(celcius):
        temp = valor + 273.15
        print(f'a temperatura {valor}C indice {ind+1}, ficou #{temp} em kelvin')
celsius = [25, 30, 15, 10]
converter(celsius)
