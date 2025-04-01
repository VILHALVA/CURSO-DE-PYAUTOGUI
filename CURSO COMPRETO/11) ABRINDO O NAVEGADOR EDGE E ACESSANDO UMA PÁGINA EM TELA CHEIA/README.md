# PROJETO: ABRINDO O NAVEGADOR EDGE E ACESSANDO UMA PÁGINA EM TELA CHEIA
Para **abrir o navegador Edge** e **acessar uma página em tela cheia** usando **PyAutoGUI**, podemos usar o **subprocess** para abrir o navegador e, em seguida, usar o PyAutoGUI para simular a interação com o teclado e o mouse.

## **Passos:**
1. **Abrir o navegador Edge**.
2. **Acessar uma URL**.
3. **Colocar o navegador em tela cheia**.

Aqui está o código para realizar esses passos:

## **1. Instalando o PyAutoGUI**
Se você ainda não tem o **PyAutoGUI** instalado, use o seguinte comando:

```bash
pip install pyautogui
```

## **2. Código para Abrir o Navegador e Acessar uma Página**
Crie um arquivo chamado **`CODIGO.py`** e adicione o seguinte código:

```python
import pyautogui
import subprocess
import time

# Caminho do navegador Edge. Ajuste o caminho conforme necessário no seu sistema.
caminho_edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# URL que você quer acessar
url = 'https://www.exemplo.com'  # Substitua pela URL que você deseja abrir

# Abrir o navegador Edge
subprocess.Popen([caminho_edge, url])

# Espera 5 segundos para o navegador abrir
time.sleep(5)

# Simula a tecla F11 para colocar a janela em tela cheia
pyautogui.press('f11')

# Espera 3 segundos para garantir que a tela cheia foi ativada
time.sleep(3)

# Aqui você pode adicionar interações extras, como clicar em elementos na página, etc.
```

## **3. Como Funciona o Código**
- **`subprocess.Popen([caminho_edge, url])`** → Abre o navegador Edge e acessa a URL especificada.
- **`time.sleep(5)`** → Dá tempo para o navegador abrir e carregar a página.
- **`pyautogui.press('f11')`** → Simula o pressionamento da tecla **F11**, que coloca o navegador em tela cheia.
- **`time.sleep(3)`** → Espera um tempo para garantir que o navegador foi colocado em tela cheia.

## **4. Ajustando o Caminho do Navegador**
- O caminho do navegador pode variar dependendo do seu sistema. No exemplo acima, foi usado o caminho padrão para o Windows. 
  - Se você estiver no **Windows**, geralmente o caminho do Edge é:
    - `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`
  - Para **Mac** ou **Linux**, o caminho será diferente, mas você pode encontrá-lo com o seguinte comando no terminal:
    - **Mac**: `which microsoft-edge`
    - **Linux**: `which microsoft-edge`

## **5. Teste e Personalização**
- Se você quiser usar outra tecla para maximizar o navegador (caso o F11 não funcione por algum motivo), pode tentar outras teclas como **`win`** + **`up`** para maximizar a janela.

## **🔍 Explicações Adicionais**
- **PyAutoGUI** não tem suporte direto para abrir navegadores, então usamos **`subprocess.Popen()`** para chamar o navegador e acessar a URL.
- A tecla **F11** é um atalho comum para colocar a maioria dos navegadores em tela cheia, incluindo o Microsoft Edge.

## **🎯 Desafios Extras**
1️⃣ **Automatizar a navegação em uma página**: Após abrir a página, você pode usar o PyAutoGUI para clicar em links, preencher formulários ou interagir com a página.
2️⃣ **Usar PyAutoGUI para simular um preenchimento automático de formulário**: Após a abertura da página, use o PyAutoGUI para simular a entrada de texto em campos de formulário.

