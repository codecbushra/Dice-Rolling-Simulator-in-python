from tkinter import *
import random
root = Tk()
root.title("Dice Rolling Simulator")
root.geometry("600x600")
titlelabel=Label(root,font='Helvetica 35 bold italic',text="Dice Rolling Simulator",fg='crimson')
titlelabel.pack()
Dicelabel=Label(root,font=('Helvetica',300,'bold'),text="",fg='deeppink')
Dicelabel.pack()

def rollDice():
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    Dicelabel.configure(text=f'{random.choice(dice)}')

buttonRollDice=Button(root,font=('Helvetica 25 bold italic'),text="Roll Dice",command=rollDice, fg='crimson',bg='orchid')
buttonRollDice.pack()

root.mainloop()
