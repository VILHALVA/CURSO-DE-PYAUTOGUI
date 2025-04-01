# PROJETO: MANIPULANDO JANELAS COM PYAUTOGUI E PYGETWINDOW
Para **manipular janelas** em sistemas operacionais como o Windows, **PyAutoGUI** não possui funcionalidades nativas para interagir diretamente com janelas (como mover, redimensionar ou maximizar). No entanto, você pode usar o **PyAutoGUI em conjunto com outras bibliotecas**, como o **pygetwindow**, para controlar janelas de aplicativos.

Aqui está um exemplo prático de como **abrir, manipular e interagir com janelas** utilizando PyAutoGUI e pygetwindow.

Neste projeto, vamos:
1. **Abrir uma janela específica.**
2. **Maximizar, minimizar ou mover a janela.**
3. **Usar o PyAutoGUI para interagir com os elementos da janela.**

## **📄 1. Passos Antes de Executar**  
1️⃣ **Instale a biblioteca `pygetwindow`** que vai permitir manipular as janelas do sistema:  

```bash
pip install pygetwindow
```

2️⃣ **Abra a janela ou o aplicativo que deseja manipular** antes de executar o script.  
   
## **📄 2. Código do Projeto**  
Crie um arquivo **`CODIGO.py`** e adicione o seguinte código:

```python
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
```

## **🚀 3. Como Executar**  
1️⃣ **Abra o aplicativo desejado (ex: Bloco de Notas ou outro aplicativo)**.  
2️⃣ **Execute o script** para que ele manipule a janela de acordo com as instruções:
   ```bash
   python CODIGO.py
   ```

## **🔍 Explicação do Código**  
✔ **`gw.getWindowsWithTitle('Bloco de Notas')`** → Retorna todas as janelas abertas que têm o título especificado (no caso, 'Bloco de Notas'). Você pode usar o título de qualquer janela.  
✔ **`janela.maximize()`** → Maximiza a janela.  
✔ **`janela.moveTo(x, y)`** → Move a janela para a posição `(x, y)` na tela.  
✔ **`janela.minimize()`** → Minimiza a janela.  
✔ **`janela.restore()`** → Restaura a janela, se estiver minimizada.  
✔ **`janela.activate()`** → Foca na janela, tornando-a ativa para interação.  
✔ **`pyautogui.write('Texto automatizado!')`** → Usa o PyAutoGUI para escrever um texto na janela ativa.

## **🎯 Desafios Extras**  
1️⃣ **Crie uma função que maximize uma janela e depois tire uma captura de tela dela**.  
2️⃣ **Automatize a interação com várias janelas**, movendo uma para um lado da tela e outra para o outro.  
3️⃣ **Faça o script interagir com um aplicativo específico**. Por exemplo, simule um clique em um botão de um software.  

## **📍 Dicas Úteis**  
- Se o título da janela que você deseja manipular não for exatamente o que você está procurando, você pode usar **strings parciais** ou fazer um loop para verificar se o título contém o texto desejado.  
- Lembre-se de que as posições `(x, y)` são coordenadas relativas à tela. As posições de janelas podem ser ajustadas com base na resolução de sua tela.
