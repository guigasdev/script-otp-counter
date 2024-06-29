import pyautogui
import cv2
import numpy as np
import time

pyautogui.FAILSAFE = False

print('Vai pra outra janela, cuida!')
time.sleep(5)

def acao_imagem1():
    pyautogui.click(200, 200)  
    print("Ação para imagem 1")

def acao_imagem2():
    pyautogui.click(200, 200)  
    print("Ação para imagem 2")

def acao_imagem3():
    pyautogui.click(200, 200)  
    print("Ação para imagem 3")  

def acao_imagem4():
    pyautogui.click(200, 200)   
    print("Ação para imagem 4")
     
imagens_acoes = {
    'pokemons/gloom.png': acao_imagem1,
    'pokemons/meowth.png': acao_imagem2,
    'pokemons/digglet.png': acao_imagem3,
    'pokemons/caterpie.png': acao_imagem4,
}

limiar = 0.8
intervalo = 0.2

# Inicializa a variável para armazenar a última imagem encontrada
ultima_imagem_encontrada = None

while True:
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)

    imagem_encontrada = False

    for imagem_referencia, acao in imagens_acoes.items():
        imagem_ref = cv2.imread(imagem_referencia, cv2.IMREAD_GRAYSCALE)
        
        if imagem_ref is None:
            print(f"Erro ao carregar a imagem {imagem_referencia}")
            continue

        altura_ref, largura_ref = imagem_ref.shape[:2]
        resultado = cv2.matchTemplate(screenshot_gray, imagem_ref, cv2.TM_CCOEFF_NORMED)
        locais = np.where(resultado >= limiar)
        
        if len(locais[0]) > 0:
            ponto = (locais[1][0], locais[0][0])
            centro = (ponto[0] + largura_ref // 2, ponto[1] + altura_ref // 2)
            
            if ultima_imagem_encontrada != imagem_referencia:
                acao()
                ultima_imagem_encontrada = imagem_referencia
                imagem_encontrada = True
            break

    if not imagem_encontrada:
        print("Procurando...")

    time.sleep(intervalo)
