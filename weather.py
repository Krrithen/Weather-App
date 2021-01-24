import requests
from bs4 import BeautifulSoup
from tkinter import *
import tkinter as tk

def update():
    global location
    getlocation=location.get()
    search = "weather in " + getlocation
    url =f"https://www.google.com/search?&q={search}"

    r = requests.get(url)
    s= BeautifulSoup(r.text,"html.parser")

    updateweather = s.find("div",class_="BNeawe").text
    mainlabel.config(text=""+updateweather)
    mainlabel1.config(text=""+getlocation.upper())
    print(updateweather)


root = Tk()
root.title("WEATHER UPDATER")
root.geometry('500x300')
root.config(bg='black')
root.resizable(False,False)


canvas = Canvas(root, width = 500, height = 400,bg="black")      
canvas.pack()      
img = PhotoImage(file="Weather.png")      
canvas.create_image(0,0,anchor=NW, image=img)


Button = Button(root,text="GET",width=5,command=update)
Button.place(x=110,y=200)

location=Entry(root,bd=5,width=20)
location.place(x=68,y=150)
location.configure(justify='center')
location.focus_set()

mainlabel = Label(root,text = " ",font =("new roman",30,"bold"),bg = "#261935",width = 4,relief = GROOVE,bd = 0,fg='white')
mainlabel.place(x=270,y=120)

mainlabel1 = Label(root,text = " ",font =("new roman",15,"bold"),bg = "#261935",width = 12,relief = GROOVE,bd = 0,fg='white')
mainlabel1.place(x=245,y=170)


root.mainloop()