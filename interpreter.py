#!/usr/bin/env python3

from os import access
import pyttsx3
import nltk
import accessapi

#initialize the tts library and set desired voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 150)     # setting up new voice rate
#engine.say("text")
#engine.runAndWait()


ON = {'value': True}
OFF = {'value': False}
greetings = ["hello", "hi", "hey"]
commands = ['lights']
def interpret(x):
    print ("interpreting " + x + "...\n")
    tokens = nltk.word_tokenize(x)
    print(tokens)
    for i in tokens:
        if i in greetings:
            engine.say("hello to you too")
            engine.runAndWait()
        if i in commands:
            print("recognized lights")
            lightStatus = accessapi.getValue()
            print(lightStatus)
            if (lightStatus):
                accessapi.toggle(OFF)
                lightStatus = False
            else:
                accessapi.toggle(ON)
                lightStatus = True
        