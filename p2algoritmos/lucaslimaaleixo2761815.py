tabuleiro=[]
continuar='s'
contp=0
contc=0
contt=0
contb=0
contrei=0
contrainha=0
iposicaorainha1=-1
jposicaorainha1=-1
iposicaorainha2=-1
jposicaorainha2=-1
linharei1=-1
colunarei1=-1
linharei2=-1
colunarei2=-1
for a in range(8):
    linha=[]
    for b in range(8):
        linha.append(0)
    tabuleiro.append(linha)
continuar='s'
while continuar == 's':
    peca=9
    i=-1
    j=-1
    while i<0 or i>7:
        i=int(input('insira a linha da posição que será preenchida: '))
    while j < 0 or j>7:
        j=int(input('insira a coluna da posição que será preenchida: '))
    while tabuleiro[i][j]!=0:
        print('posição ja tem peça!insira outra')
        i = int(input('insira a linha da posição que será preenchida: '))
        j = int(input('insira a coluna da posição que será preenchida: '))
    if contp==16:
        while peca > 6 or peca < 0 or peca==1:
            peca = int(input('essa ja foi(1-peão \n 2-cavalo \n 3-torre \n 4-bispo \n 5-rei \n 6-rainha \n 0-espaço vazio) \nescolha qual peça será inserida:'))
    elif contc==4:
        while peca > 6 or peca < 0 or peca==2:
            peca = int(input('essa ja foi(1-peão \n 2-cavalo \n 3-torre \n 4-bispo \n 5-rei \n 6-rainha \n 0-espaço vazio) \nescolha qual peça será inserida:'))
    elif contt==4:
        while peca > 6 or peca < 0 or peca == 3:
            peca = int(input('essa ja foi(1-peão \n 2-cavalo \n 3-torre \n 4-bispo \n 5-rei \n 6-rainha \n 0-espaço vazio) \nescolha qual peça será inserida:'))
    elif contb == 4:
        while peca > 6 or peca < 0 or peca == 4:
            peca = int(input('essa ja foi(1-peão \n 2-cavalo \n 3-torre \n 4-bispo \n 5-rei \n 6-rainha \n 0-espaço vazio) \nescolha qual peça será inserida:'))
    elif contrei == 2:
        while peca > 6 or peca < 0 or peca == 5:
            peca = int(input('essa ja foi(1-peão \n 2-cavalo \n 3-torre \n 4-bispo \n 5-rei \n 6-rainha \n 0-espaço vazio) \nescolha qual peça será inserida:'))
    elif contrainha == 2:
        while peca > 6 or peca < 0 or peca == 6:
            peca = int(input('essa ja foi(1-peão \n 2-cavalo \n 3-torre \n 4-bispo \n 5-rei \n 6-rainha \n 0-espaço vazio) \nescolha qual peça será inserida:'))
    else:
        while peca>6 or peca<0:
            peca=int(input('(1-peão \n 2-cavalo \n 3-torre \n 4-bispo \n 5-rei \n 6-rainha \n 0-espaço vazio) \nescolha qual peça será inserida:' ))
    if peca==1:
        contp+=1
    elif peca==2:
        contc+=1
    elif peca==3:
        contt+=1
    elif peca==4:
        contb+=1
    elif peca==5:
        contrei+=1
        if linharei1==-1:
            linharei1=i
            colunarei1=j
        elif linharei2==-1:
            linharei2=i
            colunarei2=j
    elif peca==6:
        contrainha += 1
        if iposicaorainha1==-1:
            iposicaorainha1=i
            jposicaorainha1=j
        elif iposicaorainha2==-1:
            iposicaorainha2=i
            jposicaorainha2=j
    tabuleiro[i][j]=peca
    continuar = input('deseja continuar preenchendo? (s para sim e n para não)')
    while continuar!='s' and continuar!='n':
        continuar = input('deseja continuar preenchendo? (s para sim e n para não)')
contausente=64-contp-contc-contt-contb-contrei-contrainha
for z in tabuleiro:
    print(z)
print('numero de espaços vazios:',contausente)
distanciarainhaslinhas=iposicaorainha1-iposicaorainha2
distanciarainhascolunas=jposicaorainha1-jposicaorainha2
if distanciarainhaslinhas<1:
    distanciarainhaslinhas*=-1
if distanciarainhascolunas<1:
    distanciarainhascolunas*=-1
print(f'a distancia entre as duas rainhas é de {distanciarainhaslinhas} linhas e {distanciarainhascolunas} colunas')
print(f'estão nas laterais do rei 1: {tabuleiro[linharei1-1][colunarei1]}, {tabuleiro[linharei1][colunarei1-1]}, {tabuleiro[linharei1][colunarei1+1]} e {tabuleiro[linharei1+1][colunarei1]}')
print(f'estão nas laterais do rei 2: {tabuleiro[linharei2-1][colunarei2]}, {tabuleiro[linharei2][colunarei2-1]}, {tabuleiro[linharei2][colunarei2+1]} e {tabuleiro[linharei2+1][colunarei2]}')