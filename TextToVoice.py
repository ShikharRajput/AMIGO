def main(message):

    import pyttsx3
    engine = pyttsx3.init()
    #h="shikhar will certainly slap ekta"
    #t="just shutup, chup reh"
    #engine.say("I liked it hello namashtay")
    #engine.say("Hello this is me talking to you shikhar")
    #engine.say(h)
    #engine.say(t)
    message = str(message)
    m = "You Said :" + message
    engine.say(m)

    engine.setProperty('rate',120)  #120 words per minute
    engine.setProperty('volume',0.9) 
    engine.runAndWait()
