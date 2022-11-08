hora = int(input('coloque horas: '))
min = int(input('coloque minutos: '))
if min > 60:
    print('ERRO')
else:
    dia = str(input('esta de manha ou noite: '))
    if hora > 12:
        hora = (hora - 12)
    if dia == 'manha':
        print(f'Horas: {hora}:{min} am')
    if dia == 'noite':
        print(f'Horas: {hora}:{min} pm')