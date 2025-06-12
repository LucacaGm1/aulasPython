matriz=[]
m=int(input("digite a quantidade de linhas da matriz:"))
while m<2:
    m=int(input("digite a quantidade de linhas da matriz:"))
n=int(input("digite a quantidade de colunas da matriz:"))
while n<2:
    n=int(input("digite a quantidade de linhas da matriz:"))
cont1=0
cont2=0
for i in range(m):
    vetor=[]
    for j in range(n):
        elemento=int(input(f"digite o elemento:({i+1},{j+1})"))
        if cont1==0 and cont2==0:
            if i==m-1 and j==n-2:
                while elemento!=1 and elemento!=2:
                    elemento=int(input(f"digite o elemento:({i+1},{j+1})(precisa ser 1 ou 2)"))
            elif i==m-1 and j==n-1:
                if cont1==1 and cont2==0:
                    elemento=2
                elif cont1==0 and cont2==1:
                    elemento=1
                else:
                    elemento=1
            else:
                while elemento!=1 and elemento!=0 and elemento!=2:
                    elemento=int(input(f"digite o elemento:({i+1},{j+1})"))
        elif cont1==1:
            while elemento!=0 and elemento!=2:
                elemento=int(input(f"digite o elemento:({i+1},{j+1})(não repita os elementos 1 ou 2)"))
        elif cont2==1:
            while elemento!=0 and elemento!=1:
                elemento=int(input(f"digite o elemento:({i+1},{j+1})(não repita os elementos 1 ou 2)"))
        if elemento==1:
            cont1+=1
            posicaom1=i
            posicaon1=j
        elif elemento==2:
            cont2+=1
            posicaom2=i
            posicaon2=j
        vetor.append(elemento)
    matriz.append(vetor)
distanciaentreM1e2=posicaom1-posicaom2
if distanciaentreM1e2<0:
    distanciaentreM1e2*=(-1)
distanciaentreN1e2=posicaon1-posicaon2
if distanciaentreN1e2<0:
    distanciaentreN1e2*=(-1)
for k in matriz:
    print(k)
print(f'a distância entre eles é: {distanciaentreM1e2+distanciaentreN1e2}')