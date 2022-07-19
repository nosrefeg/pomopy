import PySimpleGUI as sg
from time import sleep


sg.theme('DarkPurple')

layout = [
    [sg.Push(), sg.Text('Bem Vindo ao POMOPY, seu gerenciador de tempo feito em Python!', font=('Orbitron', 14, 'bold')), sg.Push()],
    [sg.HSep()],
    [sg.Push(), sg.Text('Escolha quantos Pomodoros deseja:', font=('Orbitron', 12)), sg.Push()],
    [sg.Push(), sg.Slider(range=(1, 20), default_value=4, key='-SLIDER-', orientation='h', size=(50, 20)), sg.Push()],
    [sg.HSep()],
    [sg.Push(), sg.Text('Escolha quantos minutos para cada Pomodoro:', font=('Orbitron', 12)), sg.Push()],
    [sg.Push(), sg.Push(), sg.Button('20', key='-20-'), sg.Push(), sg.Button('25', key='-25-'), sg.Push(), sg.Button('30', key='-30-'), sg.Push(), sg.Push()],
    [sg.HSep()],
    [sg.Push(), sg.Button('INICIAR', key='-INICIAR-', size=(10, 2)), sg.Button('CANCELAR', key='-CANCELAR-', size=(10, 2)), sg.Push()],
    [sg.Push(), sg.Text('POMODOROS:', font=('Orbitron', 12)),sg.Text('', key='-POMODOROS-'),sg.VSep(), 
    sg.Text('MINUTOS:', font=('Orbitron', 12)),sg.Text('', key='-MINUTOS-'), sg.Push()],
    [sg.Push(), sg.Text('', enable_events=True, key='-TEXTO-', font=('Orbitron', 40, 'bold')), sg.Push()],
    # [sg.HSeparator()]
]

minutos = 0
window = sg.Window('POMOPY', size=(800, 500), layout=layout, font=('Orbitron', 10))

while True:
    event, values = window.read()

    pomodoros = int(values['-SLIDER-'])

    # if event in ('-20-', '-25-', '-30-', '-INICIAR-'):
    #     window[f'{event}'].update(button_color='purple')
    #     window.refresh()

    match(event):
        case '-20-':
            minutos = 20
        case '-25-':
            minutos = 25
        case '-30-':
            minutos = 30
    
    print(pomodoros)
    print(minutos)

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
    elif event == '-INICIAR-':
        for pomodoros in range(0, pomodoros):  #  loop com a quantidade de pomodoros escolhida
            if minutos == 20:  # loops de temporizador, de acordo com a minutagem escolhida
                for i in range(minutos, 0, -1):
                    window['-TEXTO-'].update(f'{i}')
                    window.refresh()
                    sleep(60)
                for i in range(5, 0, -1):  # tempo de descanso entre cada pomodoro 
                    if pomodoros % 4 == 0: #  verifica se os pomodoros chegaram a 4 ou múltiplos, e pula a execução
                        continue
                    else:
                        window['-TEXTO-'].update(f'{i} minutos de descanso')
                        window.refresh()
                        sleep(60)
            elif minutos == 25:
                for i in range(minutos, 0, -1):
                    window['-TEXTO-'].update(i)
                    window.refresh()
                    sleep(60)
                for i in range(7, 0, -1):
                    if pomodoros % 4 == 0:
                        continue
                    else:
                        window['-TEXTO-'].update(f'{i} minutos de descanso')
                        window.refresh()
                        sleep(60)
            elif minutos == 30:
                for i in range(minutos, 0, -1):
                    window['-TEXTO-'].update(i)
                    window.refresh()
                    sleep(60)
                for i in range(10, 0, -1):
                    if pomodoros % 4 == 0:
                        continue
                    else:
                        window['-TEXTO-'].update(f'{i} minutos de descanso')
                        window.refresh()
                        sleep(60)

            if pomodoros % 4 == 0 and pomodoros != 0:
                window['-TEXTO-'].update(f'Você completou {pomodoros} pomodoros, descanse um pouco mais!')
                window.refresh()
                for i in range(20, 0, -1):
                    sleep(60)
                    if i == 1:
                        window['-TEXTO-'].update(i)
                        window.refresh()
window.close()
