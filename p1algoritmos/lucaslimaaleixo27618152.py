n1=int(input('insira o primero número:'))
while n1<0:
    n1=int(input('insira o primero número (deve ser positivo):'))
n2=int(input('insira o segundo número:'))
while n2<0:
    n2=int(input('insira o segundo número (deve ser positivo):'))
cont1=0
cont2=0
for i in range(n1,1,-1):
    resto1=n1%i
    if resto1==0:
        cont1+=1
for j in range(n2,1,-1):
    resto2=n2%j
    if resto2==0:
        cont2+=1
if cont1==1 and cont2==1:
    diferenca=n1-n2
    if diferenca==2 or diferenca==-2:
        print('são primos gêmeos')
    else:
        print('não são primos gêmeos')
else:
    print('não são primos gêmeos')