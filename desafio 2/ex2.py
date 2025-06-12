horainicial=int(input('insira a hora de início:'))
minutoinicial=int(input('insira a minuto de início:'))
horafinal=int(input('insira a hora final:'))
minutofinal=int(input('insira o minuto final:'))
if horainicial>horafinal:
    tempoh=(24-horainicial)+horafinal
    tempomin=minutofinal-minutoinicial
    if tempomin<0:
        tempoh=tempoh-1
        tempomin=60-tempomin
else:
    tempoh=horafinal-horainicial
    tempomin=minutofinal-minutoinicial
    if tempomin<0:
        tempoh=tempoh-1
        tempomin=60-tempomin
print('O jogo durou',tempoh,'horas e',tempomin,'minutos.')