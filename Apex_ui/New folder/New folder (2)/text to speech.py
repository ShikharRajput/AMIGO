from gtts import gTTS
import os
mytext = "Hello World!"
language = 'en'
myobj = gTTS(text=mytext,lang=language, slow=False)
myobj.save('hello.wav')
os.system("hello.wav")
