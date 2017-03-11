import os
import time
import webbrowser
content='''dim speechobject
set speechobject=createobject("sapi.spvoice")
speechobject.speak "Hey Abhinav, what's your plan for this valentine? would you like to go on a date with me? Wait let me play your favourite song"'''
say=open('speech.vbs','w+')
say.write(content)
say.close()
text_file='speech.vbs'
#for i in range(3):
os.startfile(text_file)
time.sleep(10)
webbrowser.open('https://www.youtube.com/watch?v=i_yLpCLMaKk')
