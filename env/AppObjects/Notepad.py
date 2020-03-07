from pywinauto.application import Application


def start_notepad_app(context):
    Application(backend="uia").start('notepad.exe')    