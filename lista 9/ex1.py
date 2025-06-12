n=int(input('insira o número de cofres: '))
cofres=[]
saldo=float(input(f'insira quantos galeões estão no cofre 1: '))
soma=saldo
maiorsaldo=saldo
menorsaldo=saldo
posicaomenor=1
posicaomaior=1
for i in range(n-1):
    saldo=float(input(f'insira quantos galeões estão no cofre {i+2}: '))
    cofres.append(saldo)
    soma+=saldo
    if saldo>maiorsaldo:
        maiorsaldo=saldo
        posicaomaior=i+2
    elif saldo<menorsaldo:
        menorsaldo=saldo
        posicaomenor=i+2
print('\n',cofres)
print(f'\nO cofre com maior saldo é o {posicaomaior}, cujo valor é {maiorsaldo}')
print(f'O cofre com menor saldo é o {posicaomenor}, cujo valor é {menorsaldo}')