ncidades=int(input('n de cidades:'))
cidade=input('nome da cidade:')
estado=input('estado(sigla):')
nveiculos=int(input('n° de veículos de passeio:'))
acidentes_fatais=int(input('acidentes fatais:'))
acidentes=int(input('acidentes não fatais:'))
menoracidentes=acidentes_fatais
somaveiculos=nveiculos
macidentesf=acidentes_fatais
cidademenor=cidade
cidademf=cidade
menorvcidade=cidade
contrs=0
somars=0
mnveiculos=nveiculos
totalfatal=acidentes_fatais
totalnfatal=acidentes
if estado == 'RS':
    somars += acidentes
    contrs += 1
somaacidentesrs = acidentes
for i in range(ncidades-1):
    cidade=input('nome da cidade:')
    estado=input('estado(sigla):')
    nveiculos=int(input('n° de veículos de passeio:'))
    acidentes_fatais=int(input('acidentes fatais:'))
    acidentes=int(input('acidentes não fatais:'))
    #maior indice
    if acidentes_fatais>macidentesf:
        macidentesf=acidentes_fatais
        cidademf=cidade
    #menor indice
    if acidentes_fatais<menoracidentes:
        menoracidentes=acidentes_fatais
        cidademenor=cidade
    #media
    somaveiculos+=nveiculos
    #media2
    if estado=='RS':
        somars+=acidentes
        contrs+=1
    #menornpasseio
    if nveiculos<mnveiculos:
        menorvcidade=cidade
    totalfatal += acidentes_fatais
    totalnfatal += acidentes
media=somaveiculos/ncidades
porcentagem=(totalfatal/(totalfatal+totalnfatal))*100
print('maior indice de acidentes fatais:',macidentesf,', cidade:',cidademf,'menor indice de acidentes fatais:',menoracidentes,', cidade:',cidademenor)
print('média de veículos nas cidades brasileiras:',media)
if contrs!=0:
    mediars=somars/contrs
    print('média de acidentes com vítimas não fatais entre as cidades do Rio Grande do Sul:',mediars)
print('o percentual de acidentes com vítimas fatais nas cidades brasileiras:',porcentagem,'%')
print('cidade brasileira que tem o menor número de veículos de passeio:',menorvcidade)