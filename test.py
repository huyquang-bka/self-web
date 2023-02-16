from gtts import gTTS
import playsound

tts = gTTS(text='Vị trí D3', lang='vi')
tts.save("welcome.mp3")
playsound.playsound("welcome.mp3")
