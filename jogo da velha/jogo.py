matriz=[]
jogador = input('qual jogador vai começar?')
for i in range(3):
    vetor=[]
    for j in range(3):
        if i==0:
            vetor.append(j+1)
        elif i==1:
            vetor.append(j+4)
        else:
            vetor.append(j+7)
    matriz.append(vetor)

def mostrar_tabuleiro(matriz,jogador):
    for z in matriz:
        print(z)
    print(f'Jogador {jogador}, sua vez!')
    posicao=int(input(f'em qual posição você quer inserir?'))
    return posicao

def inserir(matriz,posicao,jogador):
    if posicao==1:
        matriz[0][0] = jogador
    elif posicao == 2:
        matriz[0][1] = jogador
    elif posicao == 3:
        matriz[0][2] = jogador
    elif posicao == 4:
        matriz[1][0] = jogador
    elif posicao == 5:
        matriz[1][1] = jogador
    elif posicao == 6:
        matriz[1][2] = jogador
    elif posicao == 7:
        matriz[2][0] = jogador
    elif posicao == 8:
        matriz[2][1] = jogador
    else:
        matriz[2][2] = jogador
def verificar_vitoria(matriz,jogador):
    if matriz[0][0] == matriz[0][1] == matriz[0][2] == jogador:
        return True
    elif matriz[1][0] == matriz[1][1] == matriz[1][2] == jogador:
        return True
    elif matriz[2][0] == matriz[2][1] == matriz[2][2] == jogador:
        return True
    elif matriz[0][0] == matriz[1][0] == matriz[2][0] == jogador:
        return True
    elif matriz[0][1] == matriz[1][1] == matriz[2][1] == jogador:
        return True
    elif matriz[0][2] == matriz[1][2] == matriz[2][2] == jogador:
        return True
    elif matriz[0][0] == matriz[1][1] == matriz[2][2] == jogador:
        return True
    elif matriz[0][2] == matriz[1][1] == matriz[2][0] == jogador:
        return True
    else:
        return False
for a in range(9):
    if jogador=='X' and a>0:
        jogador='O'
    elif jogador=='O' and a>0:
        jogador='X'
    inserir(matriz,mostrar_tabuleiro(matriz,jogador),jogador)
    if verificar_vitoria(matriz,jogador)==True:
        for z in matriz:
            print(z)
        print(f'Jogador {jogador} venceu!')
        break

if verificar_vitoria(matriz,jogador)==False:
    print('VELHA! Ninguém ganhou.')