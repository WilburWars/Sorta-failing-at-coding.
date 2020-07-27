import time
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import subprocess
import webbrowser
poo = print("poop")
def Apps():
    global wow
    global d2
    global chrome
    wow = r"D:\WoW\World of Warcraft\World of Warcraft Launcher"
    d2 = r"C:Users\johnb\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Steam\Destiny 2"
    chrome = r"D:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome"

def Wow_App_launch():
    global WoW_Start
    WoW_Start = tk.messagebox.askquestion ("Do you wish to start World of Warcraft?","Do you wish to start World of Warcraft?")
    if WoW_Start == "Yes":
        os.startfile(wow)
    if WoW_Start :
        print("Ok")
        time.sleep(.5)
    
def window_setup():
    window = tk.Tk()
    window.geometry("1000x1000")
    frame = tk.Frame(master=window, width=40, height=20) 
    greeting = tk.Label(text="Welcome to your application opener")
    greeting.config(font=('Time New Roman', 20))
    greeting.pack()
    window.width = '40'
    wow_open = tk.Button(window, text ="World of Warcraft", command = lambda : os.startfile(wow), width='50', height='5')
    wow_open.config(font=('Ariel', 20))
    d2_open = tk.Button(window, text ="Destiny 2", command = lambda : os.startfile(d2), width='50', height='5')
    d2_open.config(font=('Ariel', 20))
    chrome_open = tk.Button(window, text ="Chrome", command = lambda : webbrowser.open("https://www.google.com/"), width='50', height='5')
    chrome_open.config(font=('Ariel', 20))
    frame.pack()
    wow_open.pack()
    d2_open.pack()
    chrome_open.pack()
    window.mainloop()

Apps()
window_setup()

