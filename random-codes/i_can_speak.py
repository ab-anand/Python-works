# -*- coding: cp1252 -*-
#It will create a vbscript file and then open it.

import os
import time
import webbrowser
content='''Dim message, sapi
 message=InputBox("What shall I say, your Geekness?","I speak for you.")
 Set sapi=CreateObject("sapi.spvoice")
 sapi.Speak message'''
say=open('speech2.vbs','w+')
say.write(content)
say.close()
text_file='speech2.vbs'
#for i in range(3):
os.startfile(text_file)
