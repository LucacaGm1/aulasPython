def classificar_risco(idade,febre):
    if idade>65 or febre=='sim':
        return 'Risco Alto'
    elif idade>=45:
        return 'Risco Médio'
    else:
        return 'Risco Baixo'
def main():
    idade=int(input('insira a idade:'))
    while idade<0:
        int(input('insira a idade: (maior ou igual a 0)'))
    febre=input('há presença de febre? (sim/não) ')
    while febre !='sim' and febre !='nao' and febre !='não':
        febre = input('há presença de febre? (sim/não) ')
    print(classificar_risco(idade,febre))
main()