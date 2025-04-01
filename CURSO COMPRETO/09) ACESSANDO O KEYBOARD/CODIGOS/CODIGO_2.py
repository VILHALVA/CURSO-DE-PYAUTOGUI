import keyboard

# Captura uma tecla específica sendo pressionada
print("Aguardando a tecla 'a' ser pressionada...")
keyboard.wait('a')
print("A tecla 'a' foi pressionada!")

# Captura qualquer tecla sendo pressionada e executa uma ação
print("Aguardando qualquer tecla ser pressionada...")
event = keyboard.read_event()  # Espera até que uma tecla seja pressionada
print(f"A tecla pressionada foi: {event.name}")
