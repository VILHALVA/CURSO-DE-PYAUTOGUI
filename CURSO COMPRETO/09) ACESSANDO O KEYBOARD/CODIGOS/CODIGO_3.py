from pynput import keyboard

# Função que será chamada quando uma tecla for pressionada
def on_press(key):
    try:
        print(f"Tecla pressionada: {key.char}")
    except AttributeError:
        print(f"Tecla especial pressionada: {key}")

# Função que será chamada quando uma tecla for liberada
def on_release(key):
    print(f"Tecla liberada: {key}")
    if key == keyboard.Key.esc:  # Para o listener quando a tecla ESC for pressionada
        return False

# Inicializa o listener de teclado
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
