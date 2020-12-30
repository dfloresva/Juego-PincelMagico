import pyttsx3
import speech_recognition as sr

import Principal as ic

recognizer=sr.Recognizer()
microphone=sr.Microphone(device_index = 0)

eng= pyttsx3.init() 
eng.setProperty("rate",160)     #velocidad de pronunciacion
eng.setProperty("volume",2.0)   #nivel de volumen de la voz
listVoices=eng.getProperty("voices")    #Establecemos la voz a utilizar
eng.setProperty("voice",listVoices[0].id)   #Listado de voz depende de si es en pc [0,3] o lap [0,1]

eng.say("Programa de Voz Iniciado")
eng.runAndWait()
def ingresoAudio():    
    try:
        print("Reconociendo...")
        with microphone as source:
            audio = recognizer.listen(source)
            palabra=recognizer.recognize_google(audio, language="es_ES")    
        return palabra
    except: 
        return "No entiendo"

def principal():
    palabra=''
    while palabra!= "terminar":
        palabra=ingresoAudio()
        if "terminar" in palabra:
            break
        else:
            if ("iniciar" in palabra):
                print("iniciar")
                eng.say("Pizarra Magica Iniciada")
                eng.runAndWait()
                ic.PizarraVirtual()
                eng.say("Pizarra Magica Finalizada")
                eng.runAndWait()
                break
            else:
                eng.say("Texto no reconocido:")
                eng.runAndWait()
                print( "Texto no reconocido: ",palabra  )                
                
    print( "Juego Terminado") 
    eng.say("Juego terminado")
    eng.runAndWait()
principal()