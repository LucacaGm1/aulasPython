for i in range(10):
    n=int(input('insira um número:'))
    soma=0
    for x in range(n-1,0,-1):
        resto=n%x
        if resto==0:
            soma+=x
        x-=1
    if soma==n:
        print(f'{n} é um número perfeito')
    else:
        print(f'{n} não é um número perfeito')