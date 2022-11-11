def conversor(hora, min):
    
    if hora < 12:
        enviar = f'Horas: {hora}:{min} am'
    
    elif hora > 12:
        hora = (hora - 12)
        enviar = f'Horas: {hora}:{min} pm'
    saida(enviar)

def saida(mensagem):
    print(mensagem)

while True:
    hora = int(input('coloque horas: '))
    
    if hora < 0:
        print('\nfinalizado\n')
        break

    if hora > 24:
        print('\nERRO\n')
    else:
        min = int(input('coloque minutos: '))

        if min > 60:
            print('\nERRO\n')

        else:
            conversor(hora, min)
    print('\nPara sair digite hora negativa\n')
