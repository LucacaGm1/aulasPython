'''Para uma operação de criptografia é usado o determinante de matrizes 3 x 3 binárias
(apenas 0 ou 1), crie um procedimento que lê um número N dessas matrizes binárias e
retorna a soma de seus determinantes. Lembre-se de verificar se o número lido é sempre 0
ou 1, se não for é necessário ler a mesma posição novamente'''
n=int(input('insira quantas matrizes serão preenchidas: '))
somadet=0
for i in range(n):
    matriz=[]
    for j in range(3):
        vetor=[]
        for k in range(3):
            elemento = int(input('insira 0 ou 1'))
            while elemento != 0 and elemento != 1:
                elemento = int(input(f'insira 0 ou 1({j + 1},{k + 1}'))
            vetor.append(elemento)
        matriz.append(vetor)
    det=(matriz[0][0]*matriz[1][1]*matriz[2][2])+(matriz[0][1]*matriz[1][2]*matriz[2][0])+(matriz[0][2]*matriz[1][0]*matriz[2][1])-(matriz[0][2]*matriz[1][1]*matriz[2][0])-(matriz[0][1]*matriz[1][0]*matriz[2][2])-(matriz[0][0]*matriz[1][2]*matriz[2][1])
    somadet+=det
    for l in matriz:
        print(l)
print(somadet)