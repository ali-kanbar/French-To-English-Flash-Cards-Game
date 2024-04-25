from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
new_choice = None
# ---------------------------- READ THE FRENCH_WORDS FILE ------------------------------- #
try:
    words = pandas.read_csv("data/french_words.csv").to_dict(orient="records")
except FileNotFoundError:
    print("CSV file not found!Please install it")
    quit()
# ---------------------------- GENERATE WORDS ------------------------------- #
def pick_a_word():
    global new_choice
    canvas.itemconfig(canvas_image,image = card_front)
    new_choice = choice(words)
    new_word = new_choice["French"]
    while new_word == word:
        new_word = choice(words)["French"]
    canvas.itemconfig(word,text = new_choice["French"],fill = "black")
    canvas.itemconfig(language,text = "French",fill = "black")

# ---------------------------- START TURNING CARDS ------------------------------- #
def flip():
    if canvas.itemcget(language, 'text') == "French":
        canvas.itemconfig(canvas_image,image = card_back)
        canvas.itemconfig(language,text = "Englsih",fill = "white")
        canvas.itemconfig(word,text = new_choice["English"],fill = "white")
    else: 
        canvas.itemconfig(canvas_image,image = card_front)
        canvas.itemconfig(word,text = new_choice["French"],fill = "black")
        canvas.itemconfig(language,text = "French",fill = "black")
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(bg = BACKGROUND_COLOR,padx = 50,pady = 50)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.resizable(width=False, height=False)
window.title("Flashcards game")

canvas = Canvas(width=800, height= 526,bg = BACKGROUND_COLOR,highlightthickness=0)
card_front = PhotoImage(file = "images/card_front.png")
card_back = PhotoImage(file = "images/card_back.png")
canvas_image = canvas.create_image(400,263,image = card_front)
language = canvas.create_text(400,150,text = "French",font = ("Ariel",40,"italic"))
word = canvas.create_text(400,263,text = "trouve",font = ("Ariel",60,"bold"))
canvas.grid(column = 0, row = 0,columnspan=2)

pick_a_word()
flip_photo = PhotoImage(file = "images/flip.png")
flip_button = Button(image = flip_photo,highlightthickness = 0,command = flip)
flip_button.grid(row = 1,column = 1)
next_photo = PhotoImage(file = "images/next.png")
next_button = Button(image = next_photo,highlightthickness = 0,command=pick_a_word)
next_button.grid(row = 1,column = 0)


window.mainloop()