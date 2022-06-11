from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}



# FUNCTION TO PISK NEXT CARD
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)


# FLIP CARD FUNCTION
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# CREATE GUI
window = Tk()
window.title("PoliFino Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(4000, func='')

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="../../../Downloads/Solution+-+flash-card-project-end/images/card_front.png")
card_back_img = PhotoImage(file="../../../Downloads/Solution+-+flash-card-project-end/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="../../../Downloads/Solution+-+flash-card-project-end/images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command='')
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="../../../Downloads/Solution+-+flash-card-project-end/images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command='')
known_button.grid(row=1, column=1)



window.mainloop()