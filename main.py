# our main file.

''' # Reconhecedor de voz do google
import speech_recognition as sr

# Criando um reconhecedor
r = sr.Recognizer()

# Abrindo o microfone para captura
with sr.Microphone() as source:
    while True:
        audio = r.listen(source) # Define microfone como fonte de áudio
        
        if (r.recognize_google(audio, show_all=True) == []):
            print("Não disse nada.")
        else:
            print(r.recognize_google(audio, language='pt', show_all=True)['alternative'][0]['transcript'])
'''

#!/usr/bin/env python3

# prerequisites: as described in https://alphacephei.com/vosk/install and also python module `sounddevice` (simply run command `pip install sounddevice`)
# Example usage using Dutch (nl) recognition model: `python test_microphone.py -m nl`
# For more help run: `python test_microphone.py -h`

from vosk import Model, KaldiRecognizer
import os
import pyaudio

model = Model("model")
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if (rec.AcceptWaveform(data)):
        print(rec.Result())
    else:
        print(rec.PartialResult())
        
print(rec.FinalResult())