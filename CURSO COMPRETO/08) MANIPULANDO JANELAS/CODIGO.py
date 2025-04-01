import pygetwindow as gw
import pyautogui
import time

# Dê um tempo para garantir que a janela do aplicativo esteja aberta
time.sleep(2)

# Pegue a lista de todas as janelas abertas
janelas = gw.getWindowsWithTitle('Bloco de Notas')  # Altere para o título da sua janela
if janelas:
    janela = janelas[0]  # Escolhe a primeira janela com o título fornecido

    # Maximizar a janela
    janela.maximize()
    print("Janela Maximizada!")

    time.sleep(1)  # Dá um tempo para a maximização

    # Mover a janela para uma nova posição
    janela.moveTo(100, 100)
    print("Janela movida para a posição (100, 100)!")

    time.sleep(1)

    # Minimizar a janela
    janela.minimize()
    print("Janela Minimizada!")

    time.sleep(1)

    # Restaurar a janela
    janela.restore()
    print("Janela Restaurada!")

    # Focar na janela para interagir com ela
    janela.activate()

    # Usando PyAutoGUI para digitar algo na janela (se o Bloco de Notas estiver aberto)
    pyautogui.write('Texto automatizado!', interval=0.1)
    print("Texto digitado na janela!")
else:
    print("Janela não encontrada!")
