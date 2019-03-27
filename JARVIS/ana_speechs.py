#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyaudio
import speech_recognition as sr
from pygame import mixer
import os
import random
import socket
import webbrowser
import subprocess
import glob
from time import localtime, strftime
import SpeekModule
import time
import pyautogui
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

homedir = os.path.expanduser("~")
print(homedir)
doss = os.getcwd()
print(doss)
path = str(doss + '\\Musicas')
if not os.path.exists(path):
    os.mkdir(path)
path = doss + '\\Videos'
if not os.path.exists(path):
    os.mkdir(path)
	
i=0

rand = ["Oi mestre, o que posso fazer por vocee?","OlA,em que posso ajudar?","Bem vindo ao Sistema de Inteligencia Virtual,...ana falando!!!"]												   
SpeekModule.speek(rand)

def speeking():
    while i < 1:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.adjust_for_ambient_noise(source)
            print('Diga algo!')
            audio = r.listen(source)

        try:
            s = r.recognize_google(audio)
            message = s.lower().encode('utf-8')
            #print(message)		
            message = str(message)
            print(message)

            if ('tchau') in message or ('sair') in message or ('calada') in message:
                rand = ['AtE logo', '...Ana se desligando em 3, 2, 1, 0','Certo,ficarei quieta,me reative se precisar']
                SpeekModule.speek(rand)
                break
            if ('aprender') in message or ('aprenda') in message:
                rand = ['Claro senhor !!! oque vou aprender hoje ???','otimo,estava esperando que me perguntasse isso...','Vamos sim...','Espere so um minuto vou pegar lapis e papel...']
                SpeekModule.speek(rand)
                new_command = raw_input('Digite aqui o novo comando: ')
                rand = ['Certo senhor,mas o que devo responder ???']
                SpeekModule.speek(rand)
                resp = raw_input('Digite aqui uma resposta para comando recebido: ')
                rand = ['Novo comando aprendido com sucesso,Obrigado senhor ...']
                SpeekModule.speek(rand)                
            if ('oi') in message or ('olá') in message or ('olá ana') in message or ('oi ana') in message:
                rand = ['Bem vindo  ao projeto Ana inteligencia virtual a seu inteiro dispor.']
                SpeekModule.speek(rand)
            else:
                if ' ' in message:
                    rand = ['Essa frase ainda nao aprendi,devo aprender,senhor ???','Frase nova,maravilha !!!,Adoro aprender frases novas,posso anotar aqui senhor???']
                    SpeekModule.speek(rand)
                else:
                    rand = ['Esse comando deve ser novo,pois ainda nao o aprendi,devo aprender,senhor ???','Legal comando novo,devo aprender ???']
                    SpeekModule.speek(rand)				
                while i < 1:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        audio = r.adjust_for_ambient_noise(source)
                        print('Diga algo!')
                        audio = r.listen(source)

                    try:
                        s = r.recognize_google(audio)
                        message = s.lower().encode('utf-8')
                        #print(message)		
                        message = str(message)
                        print(message)
                        if ('não') in message:
                            rand = ['Ok vou ignorar isso,mas preciso que me ensine tudo,quero saber tudo...','tudo bem,so quero aprender']
                            SpeekModule.speek(rand)
                            break							
                        if ('sim') in message or ('pode') in message:
                            rand = ['Espere so um minuto vou pegar lapis e papel...']
                            SpeekModule.speek(rand)
                            rand = ['Pronto senhor,anotei aqui,mas o que devo responder ???']
                            SpeekModule.speek(rand)
                            resp = raw_input('Digite aqui uma resposta para comando recebido: ')
                            rand = ['Novo comando aprendido com sucesso,Obrigado senhor ...']
                            SpeekModule.speek(rand)
                            break
                    except sr.UnknownValueError:
                        rand = ['Nao ouvi direito,senhor !,repita por favor.','Nao entendi nada !!!','Pode repetir,senhor.']
                        print (format('Não ouvi direito,senhor!,repita por favor.'))		
                        SpeekModule.speek(rand)	
                    except sr.RequestError as e:
                        print('Não foi possível solicitar resultados$; {0}'.format(e))							
        except sr.UnknownValueError:
            rand = ['Nao ouvi direito,senhor !,repita por favor.','Nao entendi nada !!!','Pode repetir,senhor.']
            print (format('Não ouvi direito,senhor!,repita por favor.'))		
            SpeekModule.speek(rand)	
        except sr.RequestError as e:
            print('Não foi possível solicitar resultados$; {0}'.format(e))

def start():
    speeking()

if __name__ == '__main__':
	start()