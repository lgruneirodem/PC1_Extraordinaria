#https://programacionpython80889555.wordpress.com/2022/03/01/extraer-texto-de-archivos-de-video-con-python/#:~:text=audio'%20(para%20extraer%20el%20audio,y%20m%C3%A9todos%20de%20'moviepy'.
#instalar librerias
#pip install SpeechRecognition
#pip install moviepy

#importar recursos
from numpy import clip
import speech_recognition as sr
import moviepy.editor as mp
from moviepy.editor import *

"""
# loading video 
clip = VideoFileClip("Natillas.mp4")
clip = clip.subclip(0, 150)
clip.write_videofile("Natillas1.mp4")
"""

#lectura de video
clip = mp.VideoFileClip("/Users/SergioValerian/Library/CloudStorage/OneDrive-UniversidadEuropeadeMadrid/Proyecto Computacion I/Videos sin procesar/Sergio/Postres/Barritas_energeticas_saludables.mp4").subclip(195,275)

#extraemos el audio
clip.audio.write_audiofile("/Users/SergioValerian/Library/CloudStorage/OneDrive-UniversidadEuropeadeMadrid/Proyecto Computacion I/Videos procesados/Sergio Procesados/Wav/Barritas_energeticas_saludables.wav")
#iniciamos el speechrecognition
r = sr.Recognizer()

#leemos el archivo audio extraido
audio = sr.AudioFile("/Users/SergioValerian/Library/CloudStorage/OneDrive-UniversidadEuropeadeMadrid/Proyecto Computacion I/Videos procesados/Sergio Procesados/Wav/Barritas_energeticas_saludables.wav")
print("audio extraido")

#lectura de audio
with audio as source:
    r.adjust_for_ambient_noise(source)
    clean_file = r.record(source)

print("lectura terminada")
#reconocemos la voz del audio
result = r.recognize_google(clean_file,language="es-ES")
#result = r.recognize_ibm(clean_file, username="apkikey", password= "your API Key")


print("")
print(result)
#escribimos el texto en un nuevo archivo txt
with open('/Users/SergioValerian/Library/CloudStorage/OneDrive-UniversidadEuropeadeMadrid/Proyecto Computacion I/Videos procesados/Sergio Procesados/Trans/Barritas_energeticas_saludables1.txt','w') as file:
    file.write("RECOGNIZED SPEECH: \n")    
    file.write(result)

print("\nEscritura terminada")