matriz=[]
ordem=int(input("digite a ordem da matriz quadrada:"))
contnorte=0
contoeste=0
contleste=0
contsul=0
for i in range(ordem):
    vetor=[]
    for j in range(ordem):
        if i==j or i+j==ordem-1:
            elemento=0
        else:
            elemento=int(input(f"digite o elemento:({i+1},{j+1})"))
            if i<j and i+j<(ordem-1):
                contnorte+=elemento
            elif i>j and i+j<(ordem-1):
                contoeste+=elemento
            elif i<j and i+j>(ordem-1):
                contleste+=elemento
            else:
                contsul+=elemento
        vetor.append(elemento)
    matriz.append(vetor)
print(contsul)
print("\nMatriz resultante:")
for k in matriz:
    print(k)
print(f"\nSoma da região Norte: {contnorte}")
print(f"Soma da região Oeste: {contoeste}")
print(f"Soma da região Leste: {contleste}")
print(f"Soma da região Sul: {contsul}")