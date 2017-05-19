import speech_recognition as sr
import os
import webbrowser


def active_listen(): 
    r = sr.Recognizer()
    with sr.Microphone() as src:
     	audio = r.listen(src)
    global msg
    msg = ''
    try:
     msg = r.recognize_google(audio) 
     print(msg.lower())
     
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google STT; {0}".format(e))
    except:
        print("Unknown exception occurred!")
    finally:
        return msg.lower()
 
active_listen()
link=msg.split()
webbrowser.open('http://www.'+link[1].lower()+'.com')
