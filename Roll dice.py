import tkinter
import random


top = tkinter.Tk()
top.geometry('600x600')
top.title('Roll Dice')

label = tkinter.Label(top, font=('Helvetica',260))

def Roll():
     dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
     label.configure(text=f'{random.choice(dice)} {random.choice(dice)}')
     label.pack()

B = tkinter.Button(top, text="Roll Dice", command = Roll)
B.pack()
top.mainloop()






