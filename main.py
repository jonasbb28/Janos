# our main file.

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