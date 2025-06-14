import pyautogui as pa
import time
pa.PAUSE = 2

 # pyautogui.click > clicar em algum lugar
 # pyautogui.press apertar uma tecla do teclado
 # pyautogui.write > escrever um texto


# eu quero entrar no youtube e dps, eu quero que abra a aba do link do youtube, depois eu quero que vai na barra de pesquisa e pesquise gustavo gunabara modulo 5, depois arrastar o mouse até o curso e clicar para nele#
 # entao... 


#Passo 1: clicar tecla win
#Passo 2: escrever Chrome
#passo 3: clicar enter 
#Passo 4: ir ate a barra de pesquisa e colcar "https://youtube.com/"
#Passo 5: Ir até a barra de pesquisa do youtube 
#Passo 6: clicar e pesquisar "Gustavo guanabara modulo 5"
#Passo 7: arrastar o mouse até o video
#Passo 8: clicar no video



#Pronto esse é o passo a passo, que eu quero que o computador faça


pa.press('win')
pa.write('chrome')
pa.press('enter')

pa.write('https://youtube.com/')
pa.press('enter')

time.sleep(4)
pa.click(x=899, y=147)
pa.write('Gustavo guanabara modulo 5')
pa.press('enter')
time.sleep(2)
pa.click(x=749, y=710)