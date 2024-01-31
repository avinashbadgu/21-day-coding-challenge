import tkinter as tk
from tkinter import *

window = Tk()
window.title("Day 12 (WEIGHT CONVERTER)")
window.geometry("500x500")
window.configure(bg="#ADD8E6")

Label(window, text="WEIGHT CONVERTER", font=("Arial", 20), bg="black", fg='yellow').pack()

kg = tk.IntVar()

def convert_to_gram():
    kg1 = kg.get()
    gram = float(kg1) * 1000
    Label(window, text="This weight in grams would be", font=("Arial", 12)).pack()
    Label(window, text=gram, bg="#FF6347").pack()

def convert_to_ounce():
    kg1 = kg.get()
    ounce = float(kg1) * 35.274
    Label(window, text="This weight in ounce would be", font=("Arial", 12)).pack()
    Label(window, text=ounce, bg="#4682B4").pack()

def convert_to_pound():
    kg1 = kg.get()
    pound = float(kg1) * 2.20462
    Label(window, text="This weight in pound would be", font=("Arial", 12)).pack()
    Label(window, text=pound, bg="#00CED1").pack()

Label(window, text="Enter the weight in Kgs", font=("Arial", 14)).pack()
Entry(window, textvariable=kg).pack()

Button(window, text="Convert to Gram", bg="#1E90FF", command=convert_to_gram).pack()
Button(window, text="Convert to Ounce", bg="#00BFFF", command=convert_to_ounce).pack()
Button(window, text="Convert to Pound", bg="#87CEEB", command=convert_to_pound).pack()

window.mainloop()
