try:
    import tkinter
except ImportError: # python 2
    import Tkinker as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry('640x480+8+400')
mainWindow.mainloop()
