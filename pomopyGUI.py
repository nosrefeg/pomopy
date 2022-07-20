import PySimpleGUI as sg
from time import sleep
# import threading



def tempoDeEspera(window, minutos):
    """
    Função que determina o tempo de cada pomodoro(loop)
    Lê os dados da janela e os minutos que foram escolhidos pelo usuário
    :param window: Janela da aplicação
    :param minutos: (int) Tempo em minutos que define o loop, ou seja, a duração de cada pomodoro(loop)
    :return:
    """
    for i in range(minutos, 0, -1):
        window['-TEXTO-'].update(f'{i}')
        window.refresh()
        sleep(60)


def tempoDeDescanso(window, descanso = 5):
    """
    Função que determina o tempo de descanso entre cada pomodoro(loop)
    Lê os dados da janela e 
    :param window: Janela da aplicação
    :param descanso: (int) Tempo em minutos que define o loop, ou seja, tempo de descanso do usuário entre cada pomodoro(loop)
    :return:
    """
    for i in range(descanso, 0, -1):
        if descanso == 10:
            window['-TEXTO-'].update(f'Você completou um ciclo de 4 pomodoros, descanse um pouco mais!')
            window.refresh()
        window['-TEXTO-'].update(f'{i} minutos de descanso')
        window.refresh()
        sleep(60)



def pomopy():
    sg.theme('DarkPurple')

    layout = [
        [sg.Push(), sg.Text('Bem Vindo ao POMOPY, seu gerenciador de tempo feito em Python!', font=('Orbitron', 14, 'bold')), sg.Push()],
        [sg.HSep()],
        [sg.Push(), sg.Text('Escolha quantos Pomodoros deseja:', font=('Orbitron', 14)), sg.Push()],
        [sg.Push(), sg.Slider(range=(1, 20), default_value=4, key='-SLIDER-', orientation='h', size=(50, 20)), sg.Push()],
        [sg.HSep()],
        [sg.Push(), sg.Text('Escolha quantos minutos para cada Pomodoro:', font=('Orbitron', 14)), sg.Push()],
        [sg.Push(), sg.Push(), sg.Button('20', key='-20-'), sg.Push(), sg.Button('25', key='-25-'), sg.Push(), sg.Button('30', key='-30-'), sg.Push(), sg.Push()],
        [sg.HSep()],
        [sg.Push(), sg.Button('INICIAR', key='-INICIAR-', size=(10, 2)), sg.Button('CANCELAR', key='-CANCELAR-', size=(10, 2)), sg.Push()],
        [sg.Push(), sg.Text('POMODOROS:', font=('Orbitron', 14)),sg.Text('', key='-POMODOROS-'),sg.VSep(), 
        sg.Text('MINUTOS:', font=('Orbitron', 14)),sg.Text('', key='-MINUTOS-'), sg.Push()],
        [sg.Push(), sg.Text('', enable_events=True, key='-TEXTO-', font=('Orbitron', 40, 'bold')), sg.Push()],
    ]


    window = sg.Window('POMOPY', size=(800, 500), layout=layout, font=('Orbitron', 12))
    minutos = 0

    while True:
        event, values = window.read()

        pomodoros = int(values['-SLIDER-'])

        match(event):
            case '-20-':
                minutos = 20
            case '-25-':
                minutos = 25
            case '-30-':
                minutos = 30

        window['-POMODOROS-'].update(pomodoros)
        window['-MINUTOS-'].update(minutos)
        window.refresh()

        if event in (sg.WINDOW_CLOSED, sg.WIN_CLOSE_ATTEMPTED_EVENT):
            break 
        elif minutos == 0:
            continue
        elif event == '-CANCELAR-':
            minutos = 0
            pomodoros = 0
            window['-TEXTO-'].update('')
            window.refresh()

        if event == '-INICIAR-':
            for pomodoros in range(0, pomodoros):
                # threading.Thread(target=tempoDeEspera, args=(window, minutos), daemon=True).start()
                tempoDeEspera(window, minutos)
                tempoDeDescanso(window)
            if pomodoros % 4 == 0 and pomodoros != 0:
                tempoDeDescanso(window, 10)
            window['-TEXTO-'].update('Parabéns, você concluiu sua sessão!', font=('Orbitron', 30))
            window.refresh()
    window.close()

if __name__ == '__main__':
    pomopy()