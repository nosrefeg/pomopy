import PySimpleGUI as sg
from time import sleep
from threading import Thread

sg.theme('DarkPurple')


def tempoDeDescanso(window, descanso = 5):
    """
    Função que determina o tempo de descanso entre cada pomodoro(loop)
    Lê os dados da janela e faz loop para representar o tempo de descanso entre cada pomodoro
    :param window: Janela da aplicação
    :param descanso: (int) Tempo em minutos que define o loop, ou seja, tempo de descanso do usuário entre cada pomodoro(loop)
    :return:
    """
    for i in range(descanso, 0, -1):
        window['-TEMPO-'].update(f'{i}')
        window['-TEXTO-DESCANSO-'].update('MINUTOS DE DESCANSO')
        window.refresh()
        sleep(60)


def tempoDeEspera(window, minutos, pomodoros):
    """
    Função que determina o tempo de cada pomodoro(loop)
    Lê os dados da janela e os minutos que foram escolhidos pelo usuário
    :param window: Janela da aplicação
    :param minutos: (int) Tempo em minutos que define o loop, ou seja, a duração de cada pomodoro(loop)
    :return:
    """
    for i in range(0, pomodoros):
        for i in range(minutos, 0, -1):
            window['-TEMPO-'].update(f'{i}')
            window.refresh()
            sleep(60)
        tempoDeDescanso(window)
        window['-TEXTO-DESCANSO-'].update('')
    window.close()


def tela1():
    layout = [
        [sg.Push(), sg.Text('Bem Vindo ao POMOPY, seu gerenciador de tempo feito em Python!', font=('Orbitron', 14, 'bold')), sg.Push()],
        [sg.HSep()],
        [sg.Push(), sg.Text('Escolha quantos Pomodoros deseja:', font=('Orbitron', 14)), sg.Push()],
        [sg.Push(), sg.Slider(range=(1, 20), default_value=4, key='-SLIDER-', orientation='h', size=(50, 20), enable_events=True), sg.Push()],
        [sg.HSep()],
        [sg.Push(), sg.Text('Escolha quantos minutos para cada Pomodoro:', font=('Orbitron', 14)), sg.Push()],
        [sg.Push(), sg.Push(), sg.Button('20', key='-20-'), sg.Push(), sg.Button('25', key='-25-'), sg.Push(), sg.Button('30', key='-30-'), sg.Push(), sg.Push()],
        [sg.HSep()],
        [sg.Push(), sg.Button('INICIAR', key='-INICIAR-', size=(10, 2)), sg.Button('ZERAR VALORES', key='-ZERAR-', size=(10, 2)), sg.Button('SAIR', key='-SAIR-', size=(10, 2)), sg.Push()],
        [sg.Push(), sg.Text('POMODOROS:', font=('Orbitron', 14)),sg.Text('', key='-POMODOROS-'),sg.VSep(), 
        sg.Text('MINUTOS:', font=('Orbitron', 14)),sg.Text('', key='-MINUTOS-'), sg.Push()],
    ]
    return sg.Window('POMOPY', layout, location=(800,400),font=('Orbitron', 12),
                    titlebar_background_color=sg.theme_background_color(),
                    titlebar_text_color=sg.theme_text_color(),
                    titlebar_font='Orbitron', finalize=True)


def tela2():
    layout = [
        [sg.Push(), sg.Text('', key='-TEMPO-', font=('Orbitron', 40, 'bold')), sg.Push()],
        [sg.Push(), sg.Text('', key='-TEXTO-DESCANSO-', font=('Orbitron', 14, 'bold')), sg.Push()],
        [sg.HSep()],
        [sg.Push(), sg.Button('CANCELAR', key='-CANCELAR-', size=(10, 2)), sg.Push()]
    ]
    return sg.Window('POMOPY', layout, size=(300, 200),font=('Orbitron', 12),
                    titlebar_background_color=sg.theme_background_color(),
                    titlebar_text_color=sg.theme_text_color(),
                    titlebar_font='Orbitron', finalize=True)


def main():
    window1, window2 = tela1(), None
    
    minutos = pomodoros = 0
    
    while True:
        window, event, values = sg.read_all_windows()
        
        print(event, values)
        if event == '-SLIDER-':
            window['-POMODOROS-'].update(int(values['-SLIDER-']))
            pomodoros = int(values['-SLIDER-'])
            
        match(event):
            case '-20-':
                minutos = 20
            case '-25-':
                minutos = 25
            case '-30-':
                minutos = 30
        window1['-MINUTOS-'].update(minutos)
        
        if event in (sg.WINDOW_CLOSED, sg.WIN_CLOSE_ATTEMPTED_EVENT, '-SAIR-', '-CANCELAR-'):
            window.close()
            
            if window == window2:
                window2 = None
            elif window == window1:
                break
        elif event == '-INICIAR-':
            if pomodoros == 0 or minutos == 0:
                sg.popup('Verifique os valores!', 'Defina os valores para o programa!')
                continue

            window['-POMODOROS-'].update(pomodoros)
            window['-MINUTOS-'].update(minutos)
            window2 = tela2()
            
            Thread(target=tempoDeEspera, args=(window2, minutos, pomodoros), daemon=True).start()

        elif event == '-ZERAR-':
            minutos = pomodoros = 0
            window['-POMODOROS-'].update(pomodoros)
            window['-MINUTOS-'].update(minutos)


if __name__ == '__main__':
    main()
