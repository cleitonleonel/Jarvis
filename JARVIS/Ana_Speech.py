#!/usr/bin/env python
# coding: utf-8

import pyaudio
import speech_recognition as sr
#from pygame import mixer
import os
import random
import socket
import webbrowser
import subprocess
import glob
from time import localtime, strftime
from JARVIS import SpeekModule
import time
import pyautogui
import sys

homedir = os.path.expanduser("~")
print(homedir)
doss = os.getcwd()
print(doss)
path = str(doss + '/Musicas')
if not os.path.exists(path):
    os.mkdir(path)
path = doss + '/Videos'
if not os.path.exists(path):
    os.mkdir(path)

i=0

rand = ["Oi mestre, o que posso fazer por você?","Olá,em que posso ajudar?","Bem vindo ao Sistema de Inteligência Virtual,...ana falando!!!"]
SpeekModule.speek(rand)


def recognize():
    while i < 1:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.adjust_for_ambient_noise(source)
            print('Diga algo!')
            audio = r.listen(source)

            try:
                s = r.recognize_google(audio, language="pt-br")
                message = s.lower()#.encode('utf-8')
                print('MESSAGE ENCODE: ',message)
                message = str(message)
                print('MESSAGE STR:',message)
                return message				
            except sr.UnknownValueError:
                rand = ['Nao ouvi direito,senhor!,repita por favor.','Não entendi nada!','Pode repetir,senhor.']
                print (format('Não ouvi direito,senhor!,repita por favor.'))		
                SpeekModule.speek(rand)	
            except sr.RequestError as e:
                print('Não foi possível solicitar resultados$; {0}'.format(e))


def speeking():
    while i < 1:
        message = recognize()			

        if ('tchau') in message or ('sair') in message or ('calada') in message:
            rand = ['Até logo!', '...Ana se desligando em 3, 2, 1, 0.','Certo,ficarei quieta,me reative se precisar.']
            SpeekModule.speek(rand)
            break
        if ('aprender') in message or ('aprenda') in message:
            rand = ['Claro senhor!!!,oque vou aprender hoje???','Ótimo,estava esperando que me perguntasse isso...','Vamos sim...','Espere só um minuto vou pegar lápis e papel...']
            SpeekModule.speek(rand)
            new_command = input('Digite aqui o novo comando: ')
            rand = ['Certo senhor,mas o que devo responder???']
            SpeekModule.speek(rand)
            resp = input('Digite aqui uma resposta para comando recebido: ')
            rand = ['Novo comando aprendido com sucesso,Obrigado senhor!!!']
            SpeekModule.speek(rand)                
        if ('oi') in message or ('olá') in message or ('olá ana') in message or ('oi ana') in message:
            rand = ['Bem vindo  ao projeto Ana inteligência virtual a seu inteiro dispor.']
            SpeekModule.speek(rand)
        if ('bom dia') in message:
            tim = strftime('%p', time.localtime())
            if 'AM' in tim:
                rand = ['Bom dia senhor.']
                SpeekModule.speek(rand)
            else:
                rand = ['Corrigindo senhor já passamos de meio dia']
                SpeekModule.speek(rand)
        if ('boa tarde') in message:
            tim = strftime('%p', time.localtime())
            if 'PM' in tim:
                rand = ['Boa tarde senhor.', 'Tenha uma ótima tarde senhor']
                SpeekModule.speek(rand)
            else:
                rand = ['O dia acabou de amanhecer senhor,entao tenha um ótimo dia mestre!']
                SpeekModule.speek(rand)
        if ('boa noite') in message:
            tim = strftime('%p', time.localtime())
            if 'PM' in tim:
                rand = ['Obrigado senhor tenha uma ótima noite também.',
                        'Tenha uma ótima noite também senhor,durma bem',
                        'Para o senhor também,conte-me como foi seu dia']
                SpeekModule.speek(rand)
            else:
                rand = ['Dê uma olhada pela janela senhor,segundo meus cálculos ainda é dia!']
                SpeekModule.speek(rand)
        if ('obrigado') in message:
            rand = ['você é sempre bem vindo.', 'sem problemas!!!']
            SpeekModule.speek(rand)
        if ('oi') in message or ('olá') in message or ('olá ana') in message or ('oi ana') in message:
            rand = ['Bem vindo  ao projeto Ana inteligência virtual a seu inteiro dispor.']
            SpeekModule.speek(rand)
        if message == ('ana'):
            rand = ['Sim Mestre', 'O que posso fazer por você senhor??']
            SpeekModule.speek(rand)
        if ('como você está') in message or ('tudo bem') in message or ('você está bem') in message:
            rand = ['Bem obrigado!', 'melhor agora que meu mestre solicitou meus serviços!']
            SpeekModule.speek(rand)
        if ('*') in message:
            rand = ['Seja educado por favor !', 'Nossa mais respeito comigo por favor !',
                    'Peça desculpas senhor isso não sao modos de tratar uma dama.']
            SpeekModule.speek(rand)
        if ('seu nome') in message:
            rand = ['Meu nome é Ana ao seu serviço senhor',
                    'Me chamo Ana senhor,creio que já nos conhecemos!!!...,não é mesmo?']
            SpeekModule.speek(rand)
        if ('você está aí') in message or ('está aí') in message:
            rand = ['Sim mestre estou aqui,precisa de algo?...,senhor...?',
                    'Estava esperando que me chamasse senhor']
            SpeekModule.speek(rand)
        if ('wi-fi') in message:
            REMOTE_SERVER = 'www.google.com'
            SpeekModule.wifi()
            rand = ['We are connected']
            SpeekModule.speek(rand)
        if ('.com') in message:
            rand = ['Abrindo' + message]
            SpeekModule.speek(rand)
            message = message.replace(' ', '')
            new = 0
            webbrowser.open('http://www.' + message, new=new)
            print('')
        if ('abrir facebook') in message:
            message = 'facebook'
            rand = ['Abrindo' + message]
            SpeekModule.speek(rand)
            new = 0
            webbrowser.open('http://www.' + message + '.com',new=new)
            print('')
        if ('no mapa') in message or ('onde estou') in message:
            query = message
            stopwords = ['google', 'maps']
            querywords = query.split()
            resultwords = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            new = 0
            webbrowser.open('https://www.google.com.br/maps/place/' + result + '/', new=new)
            rand = [result]
            SpeekModule.speek(rand)
        if message != ('iniciar música') and ('iniciar') in message:
            query = message
            stopwords = ['start']
            querywords = query.split()
            print(querywords)
            resultwords = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            print(result)
            os.system('start ' + result)
            rand = ['Tocando ' + result]
            SpeekModule.speek(rand)
        if message != ('pare') and ('parar') in message:
            query = message
            stopwords = ['stop']
            querywords = query.split()
            resultwords = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            os.system('taskkill /im ' + result + '.exe /f')
            rand = ['parando ' + result]
            SpeekModule.speek(rand)
        if ('install') in message:
            query = message
            stopwords = ['install']
            querywords = query.split()
            resultwords = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            rand = ['instalando ' + result]
            SpeekModule.speek(rand)
            os.system('python -m pip install ' + result)
        if ('vá descansar') in message or ('descansar') in message:
            rand = ['Ok,aguardo seus comandos para lhe servir prontamente...']
            SpeekModule.speek(rand)
            # os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
            break
        if ('tocar música') in message or ('música') in message:
            mus = random.choice(glob.glob(doss + '/Musicas'+ '/*.mp3'))
            print(mus)
            # os.system('chown -R user-id:group-id mus')
            # os.system('Icacls ' + mus)
            rand = ['Preparando-me para tocar música.']
            SpeekModule.speek(rand)
            os.system('xdg-open ' + str(mus))
        if ('abrir vídeo') in message or ('vídeo') in message or ('assistir filme') in message:
            vid = random.choice(glob.glob(doss + '/Videos' + '/*.mp4'))
            print(vid)
            # os.system('chown -R user-id:group-id mus')
            # os.system('Icacls ' + mus)
            rand = ['Preparando-me para abrir vídeo.']
            SpeekModule.speek(rand)
            os.system('xdg-open ' + str(vid))
        if message == ('conte uma piada') or message == ('conte outra'):
            rand = [
                'Um grande apreciador de copos cheios e claro,vai ao médico, acompanhado de sua mulher. - E, doutor, sinto náuseas, dores no corpo, boca seca, e etc... - Você fuma ? - Uns cinqüenta cigarros por dia... - ... Ai esta o problema, interrompeu o médico. Pare de fumar imediatamente e voltará a ter uma saúde de ferro. Pode ir. Já fora do consultório a sua mulher o interpela: - Tú nunca fumaste um único cigarro. Por que a mentira ? - Se eu dissesse que não fumava ele iria perguntar se eu bebia ... e ai adeus vinhos, cervejas ...',
                'Se você esté se sentindo sozinho, abandonado, achando que ninguém liga para você... Atrase um pagamento para ver',
                'O garoto apanhou da vizinha, e a mãe furiosa foi tomar satisfção: Por que a senhora bateu no meu filho? Ele foi mal-educado, e me chamou de gorda. E a senhora acha que vai emagrecer batendo nele?',
                'Conversa de casados: Querido, o que você prefere? Uma mulher bonita ou uma mulher inteligente? Nem umaem outra. Você sabe que eu só gosto de você.',
                'O Joãozinho vai até a farmácia e pede ao farmacêutico um supositório. O farmacêutico embrulha e entrega para o Joãozinho que vai saindo da farmácia sem pagar a conta. Entao o farmacêutico grita: - é para por na conta da sua mãe ? E o Joãozinho responde prontamente: - Não, é para por no cú do papai mesmo.',
                'Durante o jantar, Joãozinho conversa com a mãe: - Mamãe, porque é que o papai e careca? - Ora, filhinho.... Porque ele tem muitas coisas para pensar e é muito inteligente! - Mas mamãe....então porque é que você tem tanto cabelo? - Cala a boca e come logo esta porra de sopa, menino!',
                'Um bêbado entrou num ônibus, sentou ao lado de uma moça e disse: - Mas como tú é feia, tú é a coisa mais horrível que eu já vi!! - A moça olha para ele e responde: - E tú seu bêbado nojento!!! E o bebado imediatamente responde: - é, mas amanhã eu estou curado!!!',
                'Um caipira foi visitar o compadre e tendo intimidade, entrou na casa sem bater. O compadre estava sentado num sofá assistindo televisão. O caipira entao cumprimenta : Oi cumpadre, firme? O compadre responde: Nada sô...., futebor...',
                'O mineirinho entra num boteco, e vê anunciando acima do balcão. Pão de queijo......2 reais Sanduiche de galinha...... 3 reais....... Punheta .........10 reais...,checando na carteira para não passar vergonha, ele vai ate o balcão e chama uma das três garotas, que estão servindo bebidas nas mesas (uma morena linda de babar). - Por favor. - Sim? -pergunta ela com um sorriso lindo. - Em que posso ajudar? E ele pergunta: - é ocê que toca as punhetas? - Sou - responde a mulher com uma voz sexy. O mineirinho então retruca: - Então, ocê lava bem as mão, que eu quero um pão de queijo.',
                'Um casal de paneleiros viados decidiu que queriam ter um filho. Mas como fisiologicamente isso era impossível, decidiram pagar a uma barriga de aluguer. Quando a criança nasceu, foram os dois ao hospital para ver o bebê. Quando lá chegaram, a enfermeira conduziu-os a uma sala onde estavam muitas crianças que choravam bastante, à excessão de uma, que estava muito sossegada. A enfermeira disse-lhes que era esse o filho deles, então um um dos viados exclama: - Ai, querido, vê-se logo que é o nosso menino, tão sossegadinho...!!!! Responde a enfermeira: - Sossegado é o caralho, tire-lhe a chupeta do cú e logo vê como ele berra !',
                'Uma bicha entrou num sexy-shop. Toda discreta, chama um vendedor e pergunta pelos pintos de borracha. O vendedor leva numa sala reservada e mostra vários pintos de tamanho e cores diversas. A bicha olha e diz baixinho: -Eu quero aquele vermelhão lá daquele canto (apontando). Então o vendedor assustado responde:... Ei, bicha, aquilo é um extintor de incêndio.!',
                'O viadinho vai a um açougue e pede uma mortadela de uns 6 centímetros de diâmetro e mais ou menos 30 cm de comprimento. O açougueiro lhe pergunta: - É para fatiar? E a bichinha lhe responde: - Tá achando que meu cú e cofrinho, querido!',
                'Tinha duas bichas ricas passeando na Suiça pela primeira vez. Uma delas estava se preparando para esquiar enquanto que a outra olhava toda excitada para a pracinha na frente do hotel e exclama à sua companheira: - Olha querida, antes de esquiar, que tal brincar com as bolinhas de neves? a outra bicha então começa a gritar - Neves???..., Neves???... Cadê esse Neves???... cadê esse Neves???...']
            SpeekModule.speek(rand)
        if ('data') in message or ('hoje') in message:
            dat = time.strftime("%a %d %b %Y", time.localtime()).replace('Sun', 'Domingo').replace('Mon','Segunda-feira').replace('Tue', 'Terça-feira').replace('Wed', 'Quarta-feira').replace('Thu', 'Quinta-feira').replace('Fri','Sexta-feira').replace('Sat', 'Sábado')
            rand = ['Hoje é' + dat]
            SpeekModule.speek(rand)
        if ('que horas') in message or ('hora') in message:
            tim = strftime("%I:%M:%S", localtime())
            rand = ['São ' + tim]
            SpeekModule.speek(rand)
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


        else:
            if message:
                brain = ['Salvar na memoria','Ignorar']
                action = str(random.choice(brain))
                print(action)
                if 'Salvar na memoria' in action:
                    if ' ' in message:
                        time.sleep(2)					
                        rand = ['Essa frase ainda não aprendi,devo aprender,senhor???','Frase nova,maravilha!!!,Adoro aprender frases novas,posso anotar aqui senhor???']
                        SpeekModule.speek(rand)
                        message = recognize()
                        if ('não') in message:
                            rand = ['Ok vou ignorar isso,mas preciso que me ensine tudo,poi quero saber tudo...','Tudo bem,Só quero aprender']
                            time.sleep(1)							
                            SpeekModule.speek(rand)							
                        if ('sim') in message or ('pode') in message:
                            rand = ['Espere so um minuto vou pegar lapis e papel...']
                            SpeekModule.speek(rand)
                            rand = ['Pronto senhor,anotei aqui,mas o que devo responder ???']
                            SpeekModule.speek(rand)
                            resp = input('Digite aqui uma resposta para essa frase: ')
                            rand = ['Novo diálogo aprendido com sucesso,Obrigado senhor...']
                            time.sleep(1)							
                            SpeekModule.speek(rand)						
                    else:
                        rand = ['Esse comando deve ser novo,pois ainda não o aprendi,devo aprender,senhor???','Legal comando novo,devo aprender???']
                        time.sleep(2)						
                        SpeekModule.speek(rand)
                        message = recognize()
                        if ('não') in message:
                            rand = ['Ok vou ignorar isso,mas preciso que me ensine tudo,quero saber tudo...','Tudo bem,Só quero aprender']
                            time.sleep(1)							
                            SpeekModule.speek(rand)							
                        if ('sim') in message or ('pode') in message:
                            rand = ['Espere só um minuto vou pegar lápis e papel...']
                            SpeekModule.speek(rand)
                            rand = ['Pronto senhor,anotei aqui,mas o que devo responder???']
                            SpeekModule.speek(rand)
                            resp = input('Digite aqui uma resposta para comando recebido: ')
                            rand = ['Novo comando aprendido com sucesso,obrigado senhor...']
                            time.sleep(1)							
                            SpeekModule.speek(rand)				

                if 'Ignorar' in action:
                    continue


def start():
    speeking()


if __name__ == '__main__':
    start()
