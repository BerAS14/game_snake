from tkinter import *

root = Tk()
c = Canvas(width=300, height=300,
           bg='white')
c.focus_set()
c.pack()

def go(x, y):

    # c.after(1000, c.move(ball, 0, -2))
    c.move(ball, x, y)
    c.after(100, go, x, y)
    # if count != 0:
    #     count -= 1
    #     go(count)

ball = c.create_oval(140, 140, 160, 160,
                     fill='green')
c.bind('<Up>',
       lambda event: go(0, -2))
c.bind('<Down>',
       lambda event: go(0, 2))
c.bind('<Left>',
       lambda event: go(-2, 0))
c.bind('<Right>',
       lambda event: go(2, 0))


root.mainloop()

