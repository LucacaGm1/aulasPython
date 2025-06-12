matriz=[]
idademaior=-1
for i in range(5):
    codigo=int(input(f"digite o código da pessoa {i+1}: "))
    idade=int(input(f"digite a idade da pessoa {i+1}: "))
    matriz.append([codigo,idade])
    if idade>idademaior:
        idademaior=idade
        codigomaior=codigo
for linha in matriz:
    print(linha)
print(f'\na pessoa mais velha tem o código {codigomaior} e tem {idademaior} anos')