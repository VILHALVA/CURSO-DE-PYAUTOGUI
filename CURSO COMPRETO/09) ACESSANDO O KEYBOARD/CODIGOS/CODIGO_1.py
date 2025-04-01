import pyautogui
import time

# Dá um tempo para preparar o aplicativo em foco
time.sleep(2)

# Simula a digitação de um texto
pyautogui.write('Olá, este é um exemplo de automação com PyAutoGUI!', interval=0.1)

# Pressiona a tecla "Enter"
pyautogui.press('enter')

# Pressiona uma combinação de teclas (Ctrl+C)
pyautogui.hotkey('ctrl', 'c')
