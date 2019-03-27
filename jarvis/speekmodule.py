#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from tempfile import TemporaryFile
from gtts import gTTS
import random
import sys
import os

#doss = os.getcwd()

def speek(rand,n):
    rand = random.choice(rand)
    os.system('mshta vbscript:Execute("CreateObject(""SAPI.SpVoice"").Speak(""'+str(rand)+'"")(window.close)")')
    #os.system('PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak'+"('"+rand+"')"+';"')
    #os.system('SayStatic.exe ' + rand)	
    #with TemporaryFile(suffix='.mp3', delete=False) as f:
        #fname = str(f.name)
        #print(fname)	
        #tts = gTTS(text=random.choice(rand), lang='pt-br')
        #tts.save(fname)
        #os.startfile(fname)		
        #mixer.pre_init() # setup mixer to avoid sound lag		
        #mixer.init()
        #mixer.music.load(fname)
        #mixer.music.play()

def wifi():
    REMOTE_SERVER = "www.google.com"
    def is_connected():
        try:
            host = socket.gethostbyname(REMOTE_SERVER)
            s = socket.create_connection((host, 80), 2)
            return True
        except:
            pass
        return False
