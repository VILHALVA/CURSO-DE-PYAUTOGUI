# MOVENDO O MOUSE 
O PyAutoGUI permite mover o cursor do mouse de maneira programada, seja de forma instantânea ou suave.  

## 📌 **1. OBTENDO A POSIÇÃO ATUAL DO MOUSE**  
Antes de mover o mouse, é útil saber sua posição na tela. Execute este código para exibir a posição em tempo real:  

```python
import pyautogui

while True:
    print(pyautogui.position())  # Exibe a posição do mouse continuamente
```

🔹 **Dica**: Execute o código, mova o mouse e observe as coordenadas no terminal.  
🔹 **Pressione `Ctrl + C` para parar a execução.**  

## 🏃‍♂️ **2. MOVENDO O MOUSE INSTANTANEAMENTE**  
Para mover o mouse para uma posição específica imediatamente:  

```python
import pyautogui

# Move o mouse para a posição (500, 300) instantaneamente
pyautogui.moveTo(500, 300)
```

## ⏳ **3. MOVENDO O MOUSE SUAVEMENTE (COM DURAÇÃO)**  
Podemos definir um tempo para a movimentação, tornando-a mais natural:  

```python
import pyautogui

# Move o mouse para a posição (500, 300) em 2 segundos
pyautogui.moveTo(500, 300, duration=2)
```

🔹 O cursor se moverá lentamente até a posição especificada.  

## 🔄 **4. MOVENDO O MOUSE RELATIVAMENTE**  
O **`moveTo()`** posiciona o mouse em coordenadas absolutas, mas podemos movê-lo **relativamente à posição atual**:  

```python
import pyautogui

# Move o mouse 100 pixels para a direita e 50 pixels para baixo
pyautogui.moveRel(100, 50, duration=1)
```

Isso significa que, independentemente de onde o cursor estiver, ele se deslocará **+100 pixels na horizontal e +50 pixels na vertical**.  

## 🎯 **5. MOVENDO O MOUSE EM UM LOOP**  

```python
import pyautogui
import time

# Move o mouse em um quadrado
for _ in range(4):
    pyautogui.moveRel(100, 0, duration=0.5)  # Direita
    pyautogui.moveRel(0, 100, duration=0.5)  # Baixo
    pyautogui.moveRel(-100, 0, duration=0.5)  # Esquerda
    pyautogui.moveRel(0, -100, duration=0.5)  # Cima
    time.sleep(1)
```

Esse código move o mouse em um **movimento quadrado**, útil para testar animações ou verificar se a automação está funcionando corretamente.  

