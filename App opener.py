import time
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import subprocess
import webbrowser
poo = print("poop")
def Apps():
    global #Insert the name of the App#
    #App 1 = File directory on the computer#
    #You can add more than one app#
    
def window_setup():
    window = tk.Tk()
    window.geometry("1000x1000")
    frame = tk.Frame(master=window, width=40, height=20) 
    greeting = tk.Label(text="Welcome to your application opener")
    greeting.config(font=('Time New Roman', 20))
    greeting.pack()
    window.width = '40'
    #Name of App_open# = tk.Button(window, text ="#App Name#", command = lambda : os.startfile(#App 1#), width='50', height='5')
    #Name of App_open#.config(font=('Ariel', 20))
    frame.pack()
    #Name of App_open#.pack()
    window.mainloop()

Apps()
window_setup()

