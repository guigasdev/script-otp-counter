import pyautogui
import cv2
import numpy as np
import time


def acao_imagem1():
    pyautogui.click(x=89, y=256)  
    print("Identifiquei o gloom")
    procurar_segunda_fase()

def acao_imagem2():
    pyautogui.click(x=89, y=256)  
    print("Identifiquei o meowth")
    procurar_segunda_fase()

def acao_imagem3():
    pyautogui.click(x=89, y=256)
    print("Identifiquei o digglet")  
    procurar_segunda_fase()

def acao_imagem4():
    pyautogui.click(x=89, y=256) 
    print("Caterpie")
    procurar_segunda_fase()

def counter_poke():
    pyautogui.click(x=89, y=256) 
    print("Soltando o Counter: Arcanine")

def counter_poke_2():
    pyautogui.click(x=89, y=256) 
    print("Soltando o Counter: Clawitzer")


imagens_acoes = {
    'pokemons/gloom.png': acao_imagem1,
    'pokemons/meowth.png': acao_imagem2,
    'pokemons/digglet.png': acao_imagem3,
    'pokemons/caterpie.png': acao_imagem4,
}

# Segunda fase de imagens e ações
imagens_acoes_segunda_fase = {
    'meus-pokemons/arcanine.png': counter_poke,
    'meus-pokemons/Clawitzer.png': counter_poke,
}

limiar = 0.8
intervalo = 0.2

ultima_imagem_encontrada = None

def procurar_segunda_fase():
    print("Procurando counter...")
    while True:
        screenshot = pyautogui.screenshot()
        screenshot_np = np.array(screenshot)
        screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)

        for imagem_referencia, acao in imagens_acoes_segunda_fase.items():
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

                acao()
                return  # Sai da segunda fase após encontrar e clicar na imagem

        print("Procurando counter...")
        time.sleep(intervalo)

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
