from time import sleep


while True:
    minutos = int(input('''Quantos minutos para cada pomodoro?
    1 - 20
    2 - 25
    3 - 30
    '''))
    pomodoros = int(input('''Quantos pomodoros?'''))

    for pomodoros in range(1, pomodoros + 1):
        if minutos == 1:
            for i in range(20, 0, -1):
                print(i)
                sleep(60)
            for i in range(5, 0, -1):
                if pomodoros % 4 == 0:
                    continue
                else:
                    print('5 minutos de descanso')
                    sleep(60)
        elif minutos == 2:
            for i in range(25, 0, -1):
                print(i)
                sleep(60)
            for i in range(7, 0, -1):
                if pomodoros % 4 == 0:
                    continue
                else:
                    print('7 minutos de descanso')
                    sleep(60)
        elif minutos == 3:
            for i in range(30, 0, -1):
                print(i)
                sleep(60)
            for i in range(10, 0, -1):
                if pomodoros % 4 == 0:
                    continue
                else:
                    print('10 minutos de descanso')
                    sleep(60)

        if pomodoros == 4:
            print(f'Você completou {pomodoros} pomodoros, descanse um pouco mais')
            for i in range(20, 0, -1):
                sleep(60)
                if i == 1:
                    print(i)

    sessao = input('Você concluiu sua sessão! Deseja continuar (S/N)? ')
    if sessao.upper() == "N":
        break
