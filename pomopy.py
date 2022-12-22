from time import sleep


while True:
    minutos = int(input('''Quantos minutos para cada pomodoro?
    1 - 20
    2 - 25
    3 - 30
    '''))
    pomodoros = int(input('''Quantos pomodoros?'''))

    for pomodoros in range(0, pomodoros):
        if minutos == 1:
            for i in range(5, 0, -1):
                print(i)
                sleep(1)
            for i in range(5, 0, -1):
                if pomodoros % 4 == 0:
                    continue
                else:
                    print(f'{i} minutos de descanso')
                    sleep(1)
        elif minutos == 2:
            for i in range(7, 0, -1):
                print(i)
                sleep(1)
            for i in range(7, 0, -1):
                if pomodoros % 4 == 0:
                    continue
                else:
                    print(f'{i} minutos de descanso')
                    sleep(1)
        elif minutos == 3:
            for i in range(10, 0, -1):
                print(i)
                sleep(1)
            for i in range(10, 0, -1):
                if pomodoros % 4 == 0:
                    continue
                else:
                    print(f'{i} minutos de descanso')
                    sleep(1)

        if pomodoros % 4 == 0:
            print(f'Você completou {pomodoros} pomodoros, descanse um pouco mais')
            for i in range(5, 0, -1):
                sleep(1)
                print(i)

    sessao = input('Você concluiu sua sessão! Deseja continuar (S/N)? ')
    if sessao.upper() == "N":
        break
