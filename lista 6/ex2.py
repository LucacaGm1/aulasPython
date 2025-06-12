ndejogadores = int(input('informe o número de jogadores:'))
ndehomens = 0
ndemulheres = 0
for i in range(ndejogadores):
    sexo = input('informe o sexo (M/F):')
    while sexo != 'M' and sexo != 'm' and sexo != 'F' and sexo != 'f':
        print('informe um valor valido')
        sexo = input('informe o sexo (M/F):')
    if sexo == 'M' or sexo == 'm':
        ndehomens = ndehomens + 1
    if sexo == 'F' or sexo == 'f':
        ndemulheres = ndemulheres + 1
print((ndehomens/ndejogadores)*100,'% são homens')
print((ndemulheres/ndejogadores)*100,'% são mulheres')
