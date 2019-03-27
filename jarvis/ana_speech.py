#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright 2010 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

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
import speekmodule
import time
import pyautogui

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
n=0

rand = ['Oi mestre, o que posso fazer por você?','Olá,em que posso ajudar?','Bem vindo ao Sistema de Inteligência Virtual,...ana falando!!!']												   
speekmodule.speek(rand,n)

INFO = '''
        +=======================================+=======================================+		
        |.......INTELLIGENCE VIRTUAL ANA........|............COMANDOS DE VOZ............|
        |               BASED                   |---------------------------------------|
        |.....JARVISE VIRTUAL INTELLIGENCE......|#bom dia      #boa tarde     #boa noite|
        +---------------------------------------+#olá      #obrigado     #como você está|
        |#Author: Valentin Genard               |#qual o seu nome?  #ana  #você está aí?|
        |#Date: 01/06/2016                      |#abrir facebook    #descansar    #tchau|		
        |#Modified by: Cleiton Leonel Creton    |#música   #site.com    #vídeo     #wifi|
        |#Date: 01/01/2017                      |#conte uma piada      #conte outra     |
        +---------------------------------------+#data      #que horas são     #encerrar|
        |#Changing the Description of this tool |#cima    #baixo    #direita   #esquerda|
        | Won't made you the coder              |#minimizar      #maximizar      #entrar|
        |#I don't take responsability for       |#subindo      #descendo     #silencioso|
        | problems of any kind                  |#aumentar volume       #diminuir volume|
        +---------------------------------------+#clique   #clique duplo  #botão direito|
        |#Alterando a descrição desta ferramenta|---------------------------------------|
        | Não fará de você o codificador        |                                       |
        |#Eu não tomo a responsabilidade por    |                                       |
        | Problemas de qualquer tipo            |                                       |
        +---------------------------------------+                                       |
        |.....JARVISE VIRTUAL INTELLIGENCE......|                                       |
        +=======================================+                                       |
        |              OPTIONS:                 |                                       |
        |#hello/hi     #goodbye    #sleep mode  |                                       |
        |#your name    #jarvis     #what time   |                                       |
        |#asite.com    #next music #music       |                                       |
        |#pause music  #wifi       #thank you   |                                       |
        |#start/stop someapp                    |                                       |
        |#pip install/uninstall anapp           |                                       |
        |#googlemaps tanyplace                  |                                       |
        +=======================================+=======================================+
        '''		
print(INFO)
# JARVIS'S EARS========================================================================================================== SENSITIVE BRAIN
                                                   # obtain audio												   
while i < 1:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.adjust_for_ambient_noise(source)
        n = n + 1
        print('Diga algo!')
        audio = r.listen(source)
                                                   # interprete de audio (Google Speech Recognition)
    try:
        s = r.recognize_google(audio)
        message = s.lower().encode('utf-8')
        #print(message)		
        message = str(message)
        print(message)
# POLITE JARVIS ============================================================================================================= BRAIN 1  												   
        if ('tchau') in message or ('sair') in message or ('calada') in message:
            rand = ['Até logo', '...Ana se desligando em 3, 2, 1, 0','Certo,ficarei quieta,me reative se precisar']
            speekmodule.speek(rand,n)
            break
        if ('aprender') in message or ('aprenda') in message:
            rand = ['Claro senhor !!! oque vou aprender hoje???','Ótimo,estava esperando que me perguntasse isso...','Vamos sim...','Espere só um minuto vou pegar lápis e papel...']
            speekmodule.speek(rand,n)			
        if ('bom dia') in message:
            tim = strftime('%p', time.localtime())
            if 'AM'	in tim:		
                rand = ['Bom dia senhor.']
                speekmodule.speek(rand,n)
            else:
                rand = ['Corrigindo senhor já passamos de meio dia']
                speekmodule.speek(rand,n)				
        if ('boa tarde') in message:
            tim = strftime('%p', time.localtime())
            if 'PM'	in tim:		
                rand = ['Boa tarde senhor.','Tenha uma ótima tarde senhor']
                speekmodule.speek(rand,n)
            else:
                rand = ['O dia acabou de amanhecer senhor,entao tenha um ótimo dia mestre!']
                speekmodule.speek(rand,n)				
        if ('boa noite') in message:
            tim = strftime('%p', time.localtime())
            if 'PM'	in tim:		
                rand = ['Obrigado senhor tenha uma ótima noite também.','Tenha uma ótima noite também senhor,durma bem','Para o senhor também,conte-me como foi seu dia']
                speekmodule.speek(rand,n)
            else:
                rand = ['Dê uma olhada pela janela senhor,segundo meus cálculos ainda é dia!']
                speekmodule.speek(rand,n)
        if ('obrigado') in message:
            rand = ['você é sempre bem vindo.', 'sem problemas!!!']
            speekmodule.speek(rand,n)
        if ('oi') in message or ('olá') in message or ('olá ana') in message or ('oi ana') in message:
            rand = ['Bem vindo  ao projeto Ana inteligência virtual a seu inteiro dispor.']
            speekmodule.speek(rand,n)			
        if message == ('ana'):
            rand = ['Sim Mestre', 'O que posso fazer por você senhor??']
            speekmodule.speek(rand,n)
        if ('como você está') in message or ('tudo bem') in message or ('você está bem') in message:
            rand = ['Bem obrigado!', 'melhor agora que meu mestre solicitou meus serviços!']
            speekmodule.speek(rand,n)
        if ('*') in message:
            rand = ['Seja educado por favor !', 'Nossa mais respeito comigo por favor !', 'Peça desculpas senhor isso não sao modos de tratar uma dama.']
            speekmodule.speek(rand,n)
        if ('seu nome') in message:
            rand = ['Meu nome é Ana ao seu serviço senhor', 'Me chamo Ana senhor,creio que já nos conhecemos!!!...,não é mesmo?']
            speekmodule.speek(rand,n)
        if ('você está aí') in message or ('está aí') in message:
            rand = ['Sim mestre estou aqui,precisa de algo?...,senhor...?', 'Estava esperando que me chamasse senhor']
            speekmodule.speek(rand,n)
# USEFUL JARVIS ============================================================================================================= BRAIN 2	
        if ('wi-fi') in message:
            REMOTE_SERVER = 'www.google.com'
            speekmodule.wifi()
            rand = ['We are connected']
            speekmodule.speek(rand,n)
        if ('.com') in message:
            rand = ['Abrindo' + message]
            speekmodule.speek(rand,n)
            message = message.replace(' ','')			
            new = 0
            webbrowser.open('http://www.' + message, new=new)
            print('')
        if ('abrir facebook') in message:
            message = 'facebook'
            rand = ['Abrindo' + message]
            speekmodule.speek(rand,n)
            new = 0
            webbrowser.open('http://www.' + message + '.com', new=new)
            print('')
        if ('no mapa') in message or ('onde estou') in message:
            query = message
            stopwords = ['google', 'maps']
            querywords = query.split()
            resultwords = [ word for word in querywords if word.lower() not in stopwords ]
            result = ' '.join(resultwords)
            new = 0
            webbrowser.open('https://www.google.com.br/maps/place/' + result + '/', new=new)
            rand = [result]
            speekmodule.speek(rand,n)
        if message != ('iniciar música') and ('iniciar') in message:
            query = message
            stopwords = ['start']
            querywords = query.split()
            print(querywords)
            resultwords = [ word for word in querywords if word.lower() not in stopwords ]
            result = ' '.join(resultwords)
            print(result)
            os.system('start ' + result)
            rand = ['Tocando ' + result]
            speekmodule.speek(rand,n)
        if message != ('pare') and ('parar') in message:
            query = message
            stopwords = ['stop']
            querywords = query.split()
            resultwords = [ word for word in querywords if word.lower() not in stopwords ]
            result = ' '.join(resultwords)
            os.system('taskkill /im ' + result + '.exe /f')
            rand = ['parando ' + result]
            speekmodule.speek(rand,n)
        if ('install') in message:
            query = message
            stopwords = ['install']
            querywords = query.split()
            resultwords = [ word for word in querywords if word.lower() not in stopwords ]
            result = ' '.join(resultwords)
            rand = ['instalando ' + result]
            speekmodule.speek(rand,n)
            os.system('python -m pip install ' + result)
        if ('vá descansar') in message or ('descansar') in message:
            rand = ['Ok,aguardo seus comandos para lhe servir prontamente...']
            speekmodule.speek(rand,n)
            #os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
            break			
        if ('tocar música') in message or ('música') in message:
            mus = random.choice(glob.glob(homedir + '\Desktop\jarvis\musicas' + '\*.mp3'))
            print(mus)           
            #os.system('chown -R user-id:group-id mus')
            #os.system('Icacls ' + mus)			
            rand = ['Preparando-me para tocar música.']
            speekmodule.speek(rand,n)
            os.system('start ' + str(mus))			
        if ('abrir vídeo') in message or ('vídeo') in message or ('assistir filme') in message:
            vid = random.choice(glob.glob(homedir + '\Desktop\jarvis\Videos' + '\*.mp4'))			
            print(vid)			
            #os.system('chown -R user-id:group-id mus')
            #os.system('Icacls ' + mus)			
            rand = ['Preparando-me para abrir vídeo.']
            speekmodule.speek(rand,n)
            os.system('start ' + str(vid))			
        if message == ('conte uma piada') or message == ('conte outra'):
            rand = ['Um grande apreciador de copos cheios e claro,vai ao médico, acompanhado de sua mulher. - E, doutor, sinto náuseas, dores no corpo, boca seca, e etc... - Você fuma ? - Uns cinqüenta cigarros por dia... - ... Ai esta o problema, interrompeu o médico. Pare de fumar imediatamente e voltará a ter uma saúde de ferro. Pode ir. Já fora do consultório a sua mulher o interpela: - Tú nunca fumaste um único cigarro. Por que a mentira ? - Se eu dissesse que não fumava ele iria perguntar se eu bebia ... e ai adeus vinhos, cervejas ...',
            'Se você esté se sentindo sozinho, abandonado, achando que ninguém liga para você... Atrase um pagamento para ver',
            'O garoto apanhou da vizinha, e a mãe furiosa foi tomar satisfção: Por que a senhora bateu no meu filho? Ele foi mal-educado, e me chamou de gorda. E a senhora acha que vai emagrecer batendo nele?',
            'Conversa de casados: Querido, o que você prefere? Uma mulher bonita ou uma mulher inteligente? Nem uma, nem outra. Você sabe que eu só gosto de você.',
            'O Joãozinho vai até a farmácia e pede ao farmacêutico um supositório. O farmacêutico embrulha e entrega para o Joãozinho que vai saindo da farmácia sem pagar a conta. Entao o farmacêutico grita: - é para por na conta da sua mãe ? E o Joãozinho responde prontamente: - Não, é para por no cú do papai mesmo.',
            'Durante o jantar, Joãozinho conversa com a mãe: - Mamãe, porque é que o papai e careca? - Ora, filhinho.... Porque ele tem muitas coisas para pensar e é muito inteligente! - Mas mamãe....então porque é que você tem tanto cabelo? - Cala a boca e come logo esta porra de sopa, menino!',
            'Um bêbado entrou num ônibus, sentou ao lado de uma moça e disse: - Mas como tú é feia, tú é a coisa mais horrível que eu já vi!! - A moça olha para ele e responde: - E tú seu bêbado nojento!!! E o bebado imediatamente responde: - é, mas amanhã eu estou curado!!!',
            'Um caipira foi visitar o compadre e tendo intimidade, entrou na casa sem bater. O compadre estava sentado num sofá assistindo televisão. O caipira entao cumprimenta : Oi cumpadre, firme? O compadre responde: Nada sô...., futebor...',
            'O mineirinho entra num boteco, e vê anunciando acima do balcão. Pão de queijo......2 reais Sanduiche de galinha...... 3 reais....... Punheta .........10 reais...,checando na carteira para não passar vergonha, ele vai ate o balcão e chama uma das três garotas, que estão servindo bebidas nas mesas (uma morena linda de babar). - Por favor. - Sim? -pergunta ela com um sorriso lindo. - Em que posso ajudar? E ele pergunta: - é ocê que toca as punhetas? - Sou - responde a mulher com uma voz sexy. O mineirinho então retruca: - Então, ocê lava bem as mão, que eu quero um pão de queijo.',
            'Um casal de paneleiros viados decidiu que queriam ter um filho. Mas como fisiologicamente isso era impossível, decidiram pagar a uma barriga de aluguer. Quando a criança nasceu, foram os dois ao hospital para ver o bebê. Quando lá chegaram, a enfermeira conduziu-os a uma sala onde estavam muitas crianças que choravam bastante, à excessão de uma, que estava muito sossegada. A enfermeira disse-lhes que era esse o filho deles, então um um dos viados exclama: - Ai, querido, vê-se logo que é o nosso menino, tão sossegadinho...!!!! Responde a enfermeira: - Sossegado é o caralho, tire-lhe a chupeta do cú e logo vê como ele berra !',
            'Uma bicha entrou num sexy-shop. Toda discreta, chama um vendedor e pergunta pelos pintos de borracha. O vendedor leva numa sala reservada e mostra vários pintos de tamanho e cores diversas. A bicha olha e diz baixinho: -Eu quero aquele vermelhão lá daquele canto (apontando). Então o vendedor assustado responde:... Ei, bicha, aquilo é um extintor de incêndio.!',
            'O viadinho vai a um açougue e pede uma mortadela de uns 6 centímetros de diâmetro e mais ou menos 30 cm de comprimento. O açougueiro lhe pergunta: - É para fatiar? E a bichinha lhe responde: - Tá achando que meu cú e cofrinho, querido!',
            'Tinha duas bichas ricas passeando na Suiça pela primeira vez. Uma delas estava se preparando para esquiar enquanto que a outra olhava toda excitada para a pracinha na frente do hotel e exclama à sua companheira: - Olha querida, antes de esquiar, que tal brincar com as bolinhas de neves? a outra bicha então começa a gritar - Neves???..., Neves???... Cadê esse Neves???... cadê esse Neves???...']
            speekmodule.speek(rand,n)
        if ('data') in message or ('hoje') in message:
            dat = time.strftime("%a %d %b %Y", time.localtime()).replace('Sun','Domingo').replace('Mon','Segunda-feira').replace('Tue','Terça-feira').replace('Wed','Quarta-feira').replace('Thu','Quinta-feira').replace('Fri','Sexta-feira').replace('Sat','Sábado')
            rand = ['Hoje é' + dat]
            speekmodule.speek(rand,n)
        if ('que horas') in message or ('hora') in message:
            tim = strftime("%I:%M:%S", localtime())
            rand = ['São ' + tim]
            speekmodule.speek(rand,n)
# POLITE JARVIS + PYAUTOGUI ============================================================================================================= BRAIN 3	
        if ('subir') in message or ('cima') in message:
            pyautogui.press('pageup')
        if ('descer') in message or ('baixo') in message:
            pyautogui.press('pagedown')
        if ('proxima') in message or ('seguinte') in message or ('pula') in message or ('direita') in message:
            pyautogui.press('right')
        if ('anterior') in message or ('esquerda') in message:
            pyautogui.press('left')
        if ('subindo') in message:
            pyautogui.press('up')
        if ('descendo') in message:
            pyautogui.press('down')
        if ('diminuir volume') in message or ('volume down') in message or ('abaixar volume') in message:
            pyautogui.press('volumedown')
        if ('aumentar volume') in message or ('volume up') in message or ('subir volume') in message:
            pyautogui.press('volumeup')
        if ('silencioso') in message or ('mudo') in message or ('silêncio') in message:
            pyautogui.press('volumemute')
        if ('entrar') in message:
            pyautogui.press('enter')
        if ('click') in message:
            pyautogui.click()
        if ('duplo') in message:
            pyautogui.click(clicks=2)
        if ('botão direito') in message or ('direito') in message:
            pyautogui.click(button='right')			
        if ('fechar') in message or ('sair') in message or ('feche') in message:
            pyautogui.hotkey('ctrl', 'w')
        if ('minimizar') in message:
            pyautogui.hotkey('win', 'm')
        if ('maximizar') in message:
            pyautogui.hotkey('win', 'shift', 'm')
        if ('encerrar programa') in message or ('encerrar') in message:
            pyautogui.hotkey('alt', 'f4')
    # exceptions			
    except sr.UnknownValueError:
        rand = ['Não ouvi direito,senhor!,repita por favor.','Não entendi nada!!!','Pode repetir,senhor.']
        print('Não ouvi direito,senhor!,repita por favor.')		
        speekmodule.speek(rand,n)	
    except sr.RequestError as e:
        print('Could not request results$; {0}'.format(e))