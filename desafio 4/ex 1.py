def fat(n):
    f=1
    for i in range(2,n+1):
        f*=i
    return f
#main
n=int(input('insira o valor de n:'))
x=float(input('insira o valor de x:'))
s=0
for i in range(n):
    expoente=2*i
    denominador=fat(2*i+1)
    y=((-1)**i)*(x**expoente)/denominador
    s+=y
print(f'o valor do somatório é: {s}')