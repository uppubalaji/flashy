import re
import tkinter as tk
from random import choice
from PIL import ImageTk, Image


# Words
en_du_dict = []
with open("./python/flashy/german_english.csv") as file:
    cotext = file.read().split("\n")
    for i in cotext:
        en_du = i.split(",")
        en_du_dict.append([en_du[0], en_du[1]])
en_du_dict.pop(0)
du_en_dict = en_du_dict
class Nxt:
    def __init__(self, dit):
        self.dit = dit
    def Next(self):
        self.textb = choice(self.dit)
        self.txta = self.textb[1]
        canvas.itemconfig(wordg, text="German:")
        canvas.itemconfig(word1, text=self.txta)
    def Mng(self):
        texte = self.textb[0]
        canvas.itemconfig(wordg, text = "English:")
        canvas.itemconfig(word1, text = texte)
    def Remove(self):
        with open("./python/flashy/know_it.csv", mode="a") as file:
                file.write(f"\n{self.textb[0]},{self.textb[1]}")

# Colors

BROWN = "#BB8D6F"
GREEN = "#ACD38B"
LIGHTGREEN = "#A1F7A7"
TCOLOR = "#E83A14"

# UI Setup

windows = tk.Tk()
windows['bg'] = LIGHTGREEN
windows.config(padx=50, pady=20)
windows.minsize(700, 500)


img1 = Image.open("./python/flashy/right.png")
right = ImageTk.PhotoImage(img1)
img2 = Image.open("./python/flashy/wrong.png")
wrong = ImageTk.PhotoImage(img2)

canvas = tk.Canvas(windows, bg=GREEN, height=350, width=600)
canvas.grid(pady=10, column=1, row=0)
wordg = canvas.create_text(300, 100, text ="", fill=TCOLOR, font = ("Times New Roman", 45, "italic"))
word1 = canvas.create_text(300, 200, text = "", font = ("Arial", 25, "bold"))

hi = Nxt(en_du_dict)

nextbtn = tk.Button(windows, text="Next", command=hi.Next)
nextbtn.grid(column=0, row=1)

rbtn = tk.Button(windows, image=right, height=100, width=100, command=hi.Remove)
rbtn.grid(column=1, row=1, pady=10)

wbtn = tk.Button(windows, text="Translate", command=hi.Mng)
wbtn.grid(column=2, row=1)

windows.mainloop()

re_dict = []
with open("python/flashy/know_it.csv") as file:
    dataq = file.read().split("\n")
    for i in dataq:
        hieq = i.split(",")
        re_dict.append([hieq[0],hieq[1]])
re_dict.pop(0)
for i in re_dict:
    du_en_dict.remove(i)
with open("./python/flashy/forgot.csv", mode = "w") as file1:
    for i in du_en_dict:
        file1.write(f"{i[0]},{i[1]}\n")