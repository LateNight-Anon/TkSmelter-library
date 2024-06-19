from tkinter import Tk, Label, Entry, Button, messagebox
from typing import List, Tuple, Dict, Callable
from threading import Thread

#error messages
class nonExistentElement(Exception): pass

global buttonDefaults, labelDefault, entryDefaults

class window(Tk):
    def loop(self): self.mainloop()
    def close(self): self.destroy()

class label:
    labelObject: Label = None
    def __init__(self, parent: Tk, xPos: int, yPos: int, txt: str) -> None:
        self.labelObject = Label(parent, text = txt, font = (labelDefaults["fontForm"], labelDefaults["fontSize"]), bg = labelDefaults["bg"], fg = labelDefaults["fg"], borderwidth = labelDefaults["borderwidth"], relief = labelDefaults["relief"])
        self.labelObject.place(x = xPos, y = yPos)

    def place(self, xPos: int, yPos: int) -> None: self.labelObject.place(x = xPos, y = yPos)
    def destroy(self) -> None: self.labelObject.destroy()
    def updateText(self, string) -> None: self.labelObject.configure(text = string)

class button:
    labelObject: Label = None
    def __init__(self, xPos: int, yPos: int, cmd: Callable, txt: str) -> None:
        self.buttonObject = Button(text = txt, font = (buttonDefaults["fontForm"], buttonDefaults["fontSize"]), bg = buttonDefaults["bg"], fg = buttonDefaults["fg"], borderwidth = buttonDefaults["borderwidth"], relief = commandDefaults["relief"], command = cmd)
        self.buttonObject.place(x = xPos, y = yPos)

    def place(self, xPos: int, yPos: int) -> None: self.buttonObject.place(x = xPos, y = yPos)
    def destroy(self) -> None: self.buttonObject.destroy()
    def updateText(self, string) -> None: self.buttonObject.configure(text = string)

class entry:
    labelObject: Label = None
    def __init__(self, xPos: int, yPos: int) -> None:
        self.entryObject = Entry(font = (entryDefaults["fontForm"], entryDefaults["fontSize"]), bg = entryDefaults["bg"], fg = entryDefaults["fg"], borderwidth = entryDefaults["borderwidth"], relief = entryDefaults["relief"])
        self.entryObject.place(x = xPos, y = yPos)

    def place(self, xPos: int, yPos: int) -> None: self.entryObject.place(x = xPos, y = yPos)
    def destroy(self) -> None: self.entryObject.destroy()
    def updateText(self, string) -> None: self.entryObject.configure(text = string)
    def getInput(self) -> str: return self.entryObject.get()

def modifyDefaults(widgetType: str, element: str, value: str | int) -> None:
        global buttonDefaults, labelDefault, entryDefaults
        match widgetType:
            case "Button":
                if element in ("relief", "bg", "fg", "text", "fontForm") and type(value) == type("aa"): buttonDefaults[element] = value
                elif element in ("fontSize", "borderwidth") and type(value) == type(1): buttonDefaults[element] = value
                else: raise nonExistentElement()
            case "Label":
                if element in ("relief", "bg", "fg", "text", "fontForm") and type(value) == type("aa"): labelDefaults[element] = value
                elif element in ("fontSize", "borderwidth") and type(value) == type(1): labelDefaults[element] = value
                else: raise nonExistentElement()
            case "Entry":
                if element in ("relief", "bg", "fg", "fontForm") and type(value) == type("aa"): buttonDefaults[element] = value
                elif element in ("fontSize", "borderwidth") and type(value) == type(1): buttonDefaults[element] = value
                else: raise nonExistentElement()
            case _: raise ValueError()

def warningMessageOnClose(titleStr: str, text: str) -> None:
    if messagebox.askquestion(title = titleStr, message = text) == "yes":
        messagebox.showinfo(title = "App is closing!", message = "App is closing!")
        exit()

def warningMessageOnClose() -> None:
    if messagebox.askquestion(title = "do you wish to close the app", message = "do you wish to close the app") == "yes":
        messagebox.showinfo(title = "App is closing!", message = "App is closing!")
        exit()

def createErrorMessage(txt: str, col: str, bgCol: str, font: str, fontSize: int, window: Tk, xPos: int, yPos: int, timer: int) -> None:
    errLabel = Label(window, text = txt, font = (font, fontSize), fg = col, bg = bgCol)
    errLabel.place(x = xPos, y = yPos)
    sleep(timer)
    errLabel.destroy()

def createWindow(size: str, resizableWidth: bool, resizableHeight: bool, name: str) -> None:
    app = window()
    app.geometry(size)
    app.resizable(width = resizableWidth, height = resizableHeight)
    app.title(name)
    return app

class abstractions:
    mean = lambda data: sum(item for item in data) / len(data)
    sumList = lambda data: sum(item for item in data)

    def display(*words) -> None:
        txt: str = ""
        for word in words: txt += word
        print(txt)

    def log(*words) -> None:
        txt: str = ""
        for word in words: txt += word
        print(txt)

    def message(titleStr: str, txt: str) -> None: messagebox.showinfo(title = titleStr, message = txt)
    def callFunctionWithThread(func: Callable) -> None: Thread(target = func).start()
    def assignOnWindowClose(window: Tk, func: Callable) -> None: window.protocol("WM_DELETE_WINDOW", func)

getInput = lambda entryWidget: entryWidget.get()

buttonDefaults = {
    "borderwidth": 0,
    "relief": "solid",
    "bg": "white",
    "fg": "black",
    "fontForm": "Arial",
    "fontSize": 15,
}

labelDefaults = {
    "borderwidth": 0,
    "relief": "solid",
    "bg": "white",
    "fg": "black",
    "fontForm": "Arial",
    "fontSize": 15
}

entryDefaults = {
    "borderwidth": 0,
    "relief": "solid",
    "bg": "white",
    "fg": "black",
    "fontForm": "Arial",
    "fontSize": 15
}