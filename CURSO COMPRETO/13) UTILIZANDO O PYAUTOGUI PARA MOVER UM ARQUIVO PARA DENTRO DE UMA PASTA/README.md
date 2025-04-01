# PROJETO: MOVER UM ARQUIVO PARA DENTRO DE UMA PASTA 
Este projeto usará **PyAutoGUI** para automatizar o processo de **mover um arquivo para dentro de uma pasta**, simulando ações humanas como **clicar e arrastar**.  

## **📂 Passos do Código**
1️⃣ **Abrir o Explorador de Arquivos** (se ainda não estiver aberto).  
2️⃣ **Localizar o arquivo que será movido**.  
3️⃣ **Clicar e arrastar o arquivo até a pasta desejada**.  
4️⃣ **Soltar o arquivo dentro da pasta**.  

## **1️⃣ Instalando o PyAutoGUI**
Se ainda não tiver instalado, execute:  
```bash
pip install pyautogui
```

## **2️⃣ Código para Mover um Arquivo para uma Pasta**
Crie um arquivo chamado **`CODIGO.py`** e cole o código abaixo:  

```python
import pyautogui
import time

# Tempo para trocar de janela antes de iniciar o script (opcional)
time.sleep(5)

# Coordenadas do arquivo e da pasta (Ajuste conforme necessário)
x_arquivo, y_arquivo = 300, 400  # Posição inicial do arquivo
x_pasta, y_pasta = 600, 400      # Posição da pasta de destino

# Clicar e segurar no arquivo
pyautogui.moveTo(x_arquivo, y_arquivo, duration=1)  # Move até o arquivo
pyautogui.mouseDown()  # Pressiona o botão do mouse

# Arrastar até a pasta
pyautogui.moveTo(x_pasta, y_pasta, duration=1)  # Move até a pasta

# Soltar o arquivo na pasta
pyautogui.mouseUp()

print("✅ Arquivo movido com sucesso!")
```

## **3️⃣ Como Funciona o Código**
✔ **`time.sleep(5)`** → Dá tempo para você trocar para a janela do Explorador de Arquivos antes da execução.  
✔ **`pyautogui.moveTo(x_arquivo, y_arquivo, duration=1)`** → Move o cursor até o arquivo.  
✔ **`pyautogui.mouseDown()`** → Simula o clique para "segurar" o arquivo.  
✔ **`pyautogui.moveTo(x_pasta, y_pasta, duration=1)`** → Move o arquivo para a pasta de destino.  
✔ **`pyautogui.mouseUp()`** → Solta o arquivo dentro da pasta.  

## **4️⃣ Como Ajustar as Coordenadas?**
1. **Ative o modo de coordenadas do PyAutoGUI** no terminal:  
   ```python
   import pyautogui
   print(pyautogui.position())
   ```
   - Mova o cursor para o **arquivo** e anote as coordenadas.  
   - Mova o cursor para a **pasta** e anote as coordenadas.  
   - Substitua os valores de `x_arquivo, y_arquivo` e `x_pasta, y_pasta` no código.  

## **5️⃣ Desafios Extras**
✅ **Mover múltiplos arquivos** → Faça um loop para mover vários arquivos seguidamente.  
✅ **Esperar até que a pasta esteja visível** → Use `pyautogui.locateOnScreen()` para identificar quando a pasta aparecer antes de arrastar o arquivo.  
✅ **Abrir o Explorador de Arquivos automaticamente** → Use `subprocess.Popen("explorer")` para abrir o explorador antes da movimentação.  

