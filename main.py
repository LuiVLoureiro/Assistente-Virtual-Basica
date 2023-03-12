import speech_recognition as sr
import os
import pyautogui
import time
from time import sleep
import pyttsx3
import pywinauto

#FALA DO PC
print('SISTEMAS LIGADOS')


#LISTA DE COMANDOS
lista_comandos = [['desligar','reiniciar'],['download filmes'], ['abrir valorant', 'escutar playlist'], ['ligar luz', 'desligar luz'], ['boleto um', 'boleto dois'], ['comandos', 'cancelar']]

faults = 3
parar = 0
audio = sr.Recognizer()

def comando_voz_usuario():
    #COMANDO PRINCIPAL PARA RECONHECIMENTO DE VOZ
    try:
        with sr.Microphone(device_index=8, sample_rate=48000, chunk_size=1024) as source:
            print("Ouvindo...")
            audio.adjust_for_ambient_noise(source, duration=0.5)
            voz = audio.listen(source, phrase_time_limit=3)
            comando = audio.recognize_google(voz, language="pt-BR",show_all=True)
            comandos = [c['transcript'].lower() for c in comando['alternative']]

            if 'desligar' in comandos:
                ROSE.desligarPC()
                
            elif 'reiniciar' in comandos:
                ROSE.reiniciarPC()

            elif 'download filmes' in comandos:
                ROSE.downloadFilmes()

            elif 'abrir valorant' in comandos:
                ROSE.abrirValorant()

            elif 'ligar luz' in comandos:
                ROSE.ligarLuz()

            elif 'desligar luz' in comandos:
                ROSE.desligarLuz()
            
            elif 'boleto um' in comandos:
                import boletos
                boletos.Boleto_Unama()
            
            elif 'boleto 2' in comandos:
                import boletos
                boletos.Boleto_Uninter()
            
            elif 'escutar playlist' in comandos:
                ROSE.escolherPlaylist()
            
            elif 'comandos' in comandos:
                import ctypes
                ctypes.windll.user32.MessageBoxW(0, f"{lista_comandos}", 0)

            elif 'cancelar' in comandos: 
                global parar
                parar = 1
        
    except:
        pass


class ROSE():
    #I.A QUE GERENCIA AS FUNCIONALIDADES DE CADA AUTOMAÇÃO

    def __init__(self):
        pass

    def desligarPC():
        os.system('shutdown -s -t 0')
    
    def reiniciarPC():
        os.system('shutdown -f -r -t 0')
    
    def downloadFilmes():
        import DOWNLOAD_FILMES
    
    def escolherPlaylist():
        import os
        import glob
        import time
        from mutagen.mp3 import MP3

        # Perguntando qual playlist deseja
        playlist = input("Qual playlist você deseja escutar? ")

        # Definindo a pasta do computador
        directory = r"C:\..."

        # Definindo a pasta da playlist
        playlist_directory = directory + '\\' + playlist + '\\'
        
        # Verificando se a pasta da playlist existe
        if os.path.exists(playlist_directory):
            # Procurando os arquivos mp3 da pasta
            files = glob.glob(playlist_directory + r"\*.mp3")

            # Executando os arquivos mp3 da pasta
            for file in files:
                os.system(f'start {file}')
                #Descobrindo a duração do arquivo de música
                info = MP3(file)
                length = info.info.length
                # Dormindo por um tempo igual a duração do arquivo
                time.sleep(length)

        # Caso a pasta da playlist não exista
        else:
            print("Essa playlist não existe.")

            
    def abrirValorant():
        conta = input('Escolha a Conta -> Thayna[1] -- Lui[2]  -> ')
        if conta == '2':
            nome_conta = ''
            senha_conta = ''
        elif conta == '1':
            nome_conta = ''
            senha_conta = ''
        
        os.system('"C:\Riot Games\Riot Client\RiotClientServices.exe" --launch-product=valorant --launch-patchline=live')
        sleep(6)
        app = pywinauto.Application().connect(path="C:\Riot Games\Riot Client\RiotClientServices.exe")
        app.top_window().edit.set_edit_text(nome_conta)
        sleep(2)
        app.top_window().edit2.set_edit_text(senha_conta)
        app.top_window().Button.click()
        sleep(5)
        app.top_window().Button0.click()
    
    def pomodoro():
        import time

        #Definindo a duração dos períodos de estudo e descanso
        estudar = 25*60  #25 minutos em segundos
        descansar = 5*60 #5 minutos em segundos
        pausa_longa = 30*60 #30 minutos em segundos

        #Definindo o limite de horas
        limite_horas = int(input("Quantas horas você deseja estudar? "))
        tempo_total = limite_horas*(60*60) #transformando as horas em segundos

        #Iniciando o ciclo de estudos
        while tempo_total > 0:
            
            # Período de estudo
            print("Comece a estudar por 25 minutos. Boa sorte!")
            time.sleep(estudar)
            tempo_total -= estudar
            
            # Período de descanso
            print("Descanse por 5 minutos. Você merece!")
            time.sleep(descansar)
            tempo_total -= descansar
            
            #A cada quatro ciclos, faça uma pausa maior
            if tempo_total % (4*estudar+4*descansar) == 0:
                print("Descanse por 30 minutos. Você merece!")
                time.sleep(pausa_longa)
                tempo_total -= pausa_longa

            #Checa se há tempo restante
            if tempo_total <= 0:
                print("Seu tempo de estudo acabou!")
                break


    def ligarLuz():
        import requests
        requests.get('LINK_DE_AUTOMAÇÃO_DA_ALEXA')
    
    def desligarLuz():
        import requests
        requests.get('LINK_DE_AUTOMAÇÃO_DA_ALEXA')


        
while True:
    if parar == 1:
        break
    else:
        while True:
            comando_voz_usuario()

    
    
