import pyttsx3
import speech_recognition as sr
#from difflib import SequenceMatcher as SM
#import random
#import time

recognizer=sr.Recognizer()
microphone=sr.Microphone(device_index = 0)

eng= pyttsx3.init()

#velocidad de pronunciacion
eng.setProperty("rate",180)
#nivel de volumen de la voz
eng.setProperty("volume",2.0)
# establecemos la voz a utilizar
listVoices=eng.getProperty("voices")
#listado de voz depende de si es en pc [0,3] o lap [0,1]
eng.setProperty("voice",listVoices[0].id)
'''
eng.say("Hola Tigre, te salio a la primera")
eng.runAndWait()
'''
palabra=""
def ingresoAudio():    
    print("Reconociendo...")
    with microphone as source:
        audio = recognizer.listen(source)
        palabra=recognizer.recognize_google(audio, language="es_ES")    
    return palabra

while palabra!= "terminar":
    palabra=ingresoAudio()
    print(palabra)


