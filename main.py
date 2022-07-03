from gtts import gTTS
from playsound import playsound

audio = 'audio.mp3'
language = 'pt-br'

texto = str(input("Digite o texto para converter em audio:"))
converter = gTTS(text = texto, lang = language, slow=False)

converter.save(audio)
playsound(audio)