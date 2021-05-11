import tkinter as tk
import random

window = tk.Tk()
# Ustawiamy rozmair okna na 400x400
window.geometry("400x400")

# Obecnie wylosowana liczba
current_random = None


def on_get_click():
    global current_random  # Wymagane "global" żeby użyć globalną zmienną
    current_random = random.randrange(0, int(entry_max.get()) + 1)
    label_message.config(text="Gotowe! Teraz spróbuj zgadnąć w polu poniżej:")


def on_guess_click():
    if int(entry_guess.get()) == current_random:
        label_message.config(text="Brawo! Zgadłeś poprawną liczbe")
    else:
        label_message.config(text="Niestety, to nie ta :( spróbuj ponownie")


label_range = tk.Label(text="Zakres liczb - od 0 do:")
entry_max = tk.Entry()
button_get = tk.Button(text="Losuj!", command=on_get_click)
label_message = tk.Label()
entry_guess = tk.Entry()
button_guess = tk.Button(text="Zgadnij", command=on_guess_click)

label_range.pack()
entry_max.pack()
button_get.pack()
label_message.pack()
entry_guess.pack()
button_guess.pack()

window.mainloop()
