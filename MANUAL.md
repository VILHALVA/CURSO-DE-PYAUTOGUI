# MANUAL
## 1. INSTALAÇÃO:  
O PyAutoGUI pode ser instalado facilmente usando o **pip**. Abra o terminal (ou CMD no Windows) e execute:  

```bash
pip install pyautogui
```

Caso queira instalar uma versão específica:  
```bash
pip install pyautogui==0.9.54
```

Se precisar atualizar:  
```bash
pip install --upgrade pyautogui
```

---

## 2. CONFIGURAÇÃO E TESTES INICIAIS:
Após a instalação, faça um teste rápido para garantir que tudo está funcionando.  

1️⃣ Abra o terminal Python digitando `python` ou `python3`.  
2️⃣ Digite os comandos abaixo para verificar se o PyAutoGUI está instalado corretamente:  

```python
import pyautogui
print(pyautogui.size())  # Retorna a resolução da tela
print(pyautogui.position())  # Mostra a posição atual do cursor
```

Se o código rodar sem erros, a instalação foi bem-sucedida.  

---

## 3. PRIMEIRO PROJETO – MOVER O MOUSE E DIGITAR AUTOMATICAMENTE:  
Crie um arquivo chamado **`automacao.py`** e adicione o seguinte código:  

```python
import pyautogui
import time

# Aguarda 3 segundos antes de começar (para dar tempo de mudar de janela)
time.sleep(3)

# Move o mouse para as coordenadas (x=500, y=300) em 2 segundos
pyautogui.moveTo(500, 300, duration=2)

# Clica na posição atual do mouse
pyautogui.click()

# Digita um texto automaticamente
pyautogui.write("Olá, mundo! Estou automatizando com PyAutoGUI.", interval=0.1)
```

### COMO EXECUTAR? 
No terminal ou CMD, navegue até a pasta onde salvou o arquivo e execute:  

```bash
python automacao.py
```

🔹 O script aguardará 3 segundos antes de iniciar (para que você possa mudar para um editor de texto, por exemplo).  
🔹 O mouse será movido automaticamente para as coordenadas `(500, 300)`.  
🔹 Um clique será realizado e o texto será digitado automaticamente.  

---

## EXTRA: CAPTURAR A POSIÇÃO DO MOUSE:
Se precisar saber as coordenadas de um ponto específico da tela, rode este código:  

```python
import pyautogui

while True:
    print(pyautogui.position())  # Mostra a posição do cursor em tempo real
```

🔹 Execute o script e mova o mouse para o local desejado.  
🔹 A posição do cursor será exibida no terminal.  
🔹 Pressione `Ctrl + C` para parar a execução.  

