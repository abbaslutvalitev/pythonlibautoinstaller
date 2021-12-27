
import pip
import subprocess
import sys
from tkinter import *
from tkinter import messagebox as mb
import _datetime
import datetime


root = Tk()
def on_closing():
    if mb.askokcancel("Quit", "Do you want to quit?"):
      root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.title("Python librarys auto installer 0.2b")
root.resizable(0, 0)
warning1 = Label(width=20, text="WARNING!", bg="red")
warning2 = Label(width=50, text="This utility in beta test! May have problems.")
en = Label(width=10, text="Library name: ")
def install(package):
   subprocess.check_call([sys.executable, "-m", "pip", "install", package])
def unistall(package):
   subprocess.check_call([sys.executable, "-m", "pip", "uninstall", package])
def upgrade(package):
   subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--upgrade"])
libname = Entry(width=20)
def onClick():
   mb.askyesno(message="Do you want to install the given library?")
   if libname.get() == None or libname.get() == "" or libname.get() == " ":
      mb.showerror(message="You did not enter the name of the library")
   else:
      lib = str(libname.get())
      install(lib)
      mb.showinfo(message="Successfully. ")
def onClick1():
   mb.askyesno(message="Do you want to uninstall the given library?")
   if libname.get() == None or libname.get() == "" or libname.get() == " ":
      mb.showerror(message="You did not enter the name of the library")
   else:
      lib = str(libname.get())
      unistall(lib)
      mb.showinfo(message="Successfully")
def onClick2():
    mb.askyesno(message="Do you want to uninstall the given library?")
    if libname.get() == None or libname.get() == "" or libname.get() == " ":
      mb.showerror(message="You did not enter the name of the library")
    else:
      lib = str(libname.get())
      upgrade(lib)
      mb.showinfo(message="Successfully")

def verinfo():
   mb.showinfo(message="Version:0.2b, Github: https://github.com/abbaslutvalitev/pythonlibautoinstaller")



installbtn = Button(width=35, text="Install!", command=onClick)
unistallbtn = Button(width=35, text="Unistall!", command=onClick1)
upgradebtn = Button(width=35, text="Upgrade!", command=onClick2)
verinfobtn = Button(width=35, text="More info!", command=verinfo)
exitbtn = Button(width=35, text="Exit!", command=on_closing)
vertext = Label(width=10, text="v0.2b")



warning1.pack()
warning2.pack()
en.pack()
libname.pack()
installbtn.pack()
unistallbtn.pack()
upgradebtn.pack()
verinfobtn.pack()
exitbtn.pack()
vertext.pack()




root.mainloop()






