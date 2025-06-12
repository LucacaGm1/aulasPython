def valordeS(n):
    s=0
    while n<4:
        n=int(input('insira um valor de N válido(>4):'))
    while n>=4:
        d=(-10)+3*n
        x=d/n
        s=s+x
        n=n-1
    return s
#main
n=int(input('insira o valor de N:'))
resultado=valordeS(n)
print(resultado)
