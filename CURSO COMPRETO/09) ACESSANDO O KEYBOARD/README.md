# ACESSANDO O KEYBOARD 
Para **acessar e manipular o teclado** em Python, podemos usar o **PyAutoGUI** para simular a digitação e pressionamento de teclas. No entanto, se você deseja capturar teclas pressionadas ou fazer interações mais avançadas com o teclado, você pode usar bibliotecas adicionais como **`keyboard`** ou **`pynput`**.

Aqui estão exemplos de como usar essas bibliotecas para acessar e manipular o teclado.

O **PyAutoGUI** permite simular a digitação e pressionamento de teclas para automatizar tarefas, como preencher formulários ou digitar texto em aplicativos.

## 📌 PROJETO 1: SIMULANDO TECLAS COM PYAUTOGUI 
### **1. Instalando o PyAutoGUI**
Se você ainda não tem o **PyAutoGUI** instalado, use o seguinte comando:

```bash
pip install pyautogui
```

### **2. Exemplo de Código para Simular a Digitação de Texto**
Crie um arquivo **`simulando_teclado.py`** e adicione o seguinte código:

```python
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
```

## 📌 PROJETO 2: CAPTURANDO TECLAS COM A BIBLIOTECA `keyboard`
A **biblioteca `keyboard`** permite que você capture pressionamentos de teclas em tempo real e execute ações baseadas neles. Isso é útil para criar sistemas de monitoramento ou comandos baseados em eventos de teclado.

### **1. Instalando a biblioteca `keyboard`**
Se você ainda não tem a **`keyboard`** instalada, use o seguinte comando:

```bash
pip install keyboard
```

### **2. Exemplo de Código para Capturar Teclas Pressionadas**
Crie um arquivo **`capturando_teclado.py`** e adicione o seguinte código:

```python
import keyboard

# Captura uma tecla específica sendo pressionada
print("Aguardando a tecla 'a' ser pressionada...")
keyboard.wait('a')
print("A tecla 'a' foi pressionada!")

# Captura qualquer tecla sendo pressionada e executa uma ação
print("Aguardando qualquer tecla ser pressionada...")
event = keyboard.read_event()  # Espera até que uma tecla seja pressionada
print(f"A tecla pressionada foi: {event.name}")
```

### **3. Funcionalidade do Código**  
- O **`keyboard.wait('a')`** espera até que a tecla 'a' seja pressionada.  
- O **`keyboard.read_event()`** captura qualquer tecla pressionada e imprime o nome da tecla.

## **📌 PROJETO 3: MONITORANDO O TECLADO COM `pynput`**
Outra opção popular para manipulação de teclado é a biblioteca **`pynput`**, que permite capturar e monitorar teclas pressionadas.

### **1. Instalando a biblioteca `pynput`**
Se você ainda não tem o **`pynput`** instalado, use o seguinte comando:

```bash
pip install pynput
```

### **2. Exemplo de Código para Monitorar Teclas com `pynput`**
Crie um arquivo **`monitorando_teclado.py`** e adicione o seguinte código:

```python
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
```

### **3. Funcionalidade do Código**  
- **`on_press(key)`** captura a tecla pressionada.  
- **`on_release(key)`** captura a tecla liberada. Se a tecla **`esc`** for pressionada, o programa para.  
- **`keyboard.Listener()`** inicializa o monitoramento do teclado e começa a capturar eventos de teclado.

## **🔍 Explicações Adicionais**  
- O **PyAutoGUI** simula pressionamentos de teclas de forma simples e eficiente, sendo útil para automações em que você deseja preencher formulários ou interagir com interfaces gráficas.  
- A **`keyboard`** permite capturar teclas pressionadas em tempo real e pode ser usada para criar programas que reagem a comandos do usuário.  
- O **`pynput`** é mais flexível, permitindo tanto monitorar teclas pressionadas quanto simular pressionamentos, além de capturar eventos como **Ctrl + C**, **Ctrl + V**, etc.

## **🎯 Desafios Extras**  
1️⃣ **Crie um programa que capture várias teclas e execute comandos diferentes com base nas teclas pressionadas.**  
2️⃣ **Use o PyAutoGUI e o `keyboard` para criar uma automação onde o script preenche um formulário e, após pressionar Enter, captura o resultado.**  
3️⃣ **Crie uma função de "hotkeys" usando o `keyboard` que execute uma função específica sempre que uma tecla combinada (como Ctrl + Alt + T) for pressionada.**

