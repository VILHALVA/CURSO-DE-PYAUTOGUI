# PROJETO: ABRIR O GOOGLE E FAZER UMA PESQUISA AUTOMÁTICA
Para **abrir a página do Google e fazer uma pesquisa automaticamente** usando **PyAutoGUI**, podemos seguir estes passos:  

1️⃣ **Abrir o navegador Microsoft Edge**  
2️⃣ **Acessar o site do Google**  
3️⃣ **Digitar um termo de pesquisa**  
4️⃣ **Pressionar "Enter" para buscar**  

## **1. Instalando o PyAutoGUI**
Se ainda não tiver o PyAutoGUI instalado, instale com o comando:  
```bash
pip install pyautogui
```

## **2. Código para Abrir o Google e Fazer uma Pesquisa**  
Crie um arquivo chamado **`CODIGO.py`** e adicione o seguinte código:  

```python
import pyautogui
import subprocess
import time

# Caminho do navegador Edge. Ajuste o caminho conforme necessário no seu sistema.
caminho_edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# URL do Google
url = 'https://www.google.com'

# Abrir o navegador e acessar o Google
subprocess.Popen([caminho_edge, url])

# Aguardar 5 segundos para o navegador abrir
time.sleep(5)

# Digitar a pesquisa no Google
pesquisa = "Automação com PyAutoGUI"
pyautogui.write(pesquisa)

# Pressionar "Enter" para buscar
pyautogui.press('enter')

# Aguardar os resultados carregarem
time.sleep(3)
```

## **3. Como Funciona o Código**
✅ **`subprocess.Popen([caminho_edge, url])`** → Abre o navegador Edge e carrega o Google.  
✅ **`time.sleep(5)`** → Dá tempo para o navegador abrir.  
✅ **`pyautogui.write(pesquisa)`** → Digita o termo de pesquisa no campo de busca.  
✅ **`pyautogui.press('enter')`** → Pressiona "Enter" para iniciar a busca.  
✅ **`time.sleep(3)`** → Espera os resultados carregarem.  

## **4. Ajustando o Caminho do Navegador**
Se o **caminho do Edge** for diferente no seu sistema, ajuste a linha:  
```python
caminho_edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
```
Você pode descobrir o caminho correto usando este comando no terminal:  
```bash
where msedge
```

## **5. Desafios Extras**
📌 **Automatizar a abertura do primeiro resultado** → Use `pyautogui.press("tab")` para navegar nos links e `pyautogui.press("enter")` para abrir o primeiro.  
📌 **Fazer pesquisas diferentes** → Modifique o valor da variável `pesquisa`.  
📌 **Adicionar espera dinâmica** → Use `pyautogui.locateOnScreen()` para detectar quando o Google estiver carregado antes de digitar.  

