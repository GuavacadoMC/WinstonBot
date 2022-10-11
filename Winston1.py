import speech_recognition
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import websockets
import base64
import asyncio
import json
from math import *
from neuralintents import GenericAssistant
import sys


i = 1
engine = pyttsx3.init()  # speaks to the user
recognizer = sr.Recognizer()  # listens for commands

engine.say("I will speak this text")
engine.runAndWait()


def calculate():
    time = datetime.datetime.now().strftime('%I:%M %p')
    engine.say('Current time is ' + time)
    print('Current time is ' + time)
    engine.runAndWait()

def greetings():
    engine.say('Hello sir, how may I be of service?')
    print('Hello sir, how may I be of service?')
    engine.runAndWait()
    try:
        with sr.Microphone() as mic:  # opens the file to use my Microphone as input
            print('Listening..')  # prints that the bot is listening for any commands
            voice = recognizer.listen(mic)  # the audio that comes from the source
            say = recognizer.recognize_google(voice)  # this is what I say.
            if 'time' in say:
                calculate()
    except:
        pass
    if "What is one plus two?" in say:
        calculate()

def call():


        try:
            with sr.Microphone() as mic:  # opens the file to use my Microphone as input
                print('Listening..')  # prints that the bot is listening for any commands
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                voice = recognizer.listen(mic)  # saves audio from the mic into this variable
                say = recognizer.recognize_google(voice)  # this is what I say.
                say = say.lower()
        except:
            pass


with sr.Microphone() as mic:  # opens the file to use my Microphone as input
    print('Listening..')  # prints that the bot is listening for any commands
    voice = recognizer.listen(mic)  # the audio that comes from the source
    say = recognizer.recognize_google(voice)  # this is what I say.




call()
if 'hello' in say:
    print(say)
    greetings()



