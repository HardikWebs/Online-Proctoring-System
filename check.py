from tkinter import *

def error():
   error_win = Tk()
   error_win.geometry('250x70')
   message = Label(error_win, text='WARNING! Potential cheating detected.')
   message.pack()
   error_win.mainloop()

error()