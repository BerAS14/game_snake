from tkinter import Tk, Canvas

from gameSnake import GameSnake

root = Tk()
c = Canvas(width=1000, height=1000,
           bg='white')
c.focus_set()
c.pack()

def go():
    c.move(snake, game.x, game.y)
    c.after(100, go)



snake = c.create_rectangle(400, 400, 430, 430, fill='green')
# ball = c.create_oval(40, 140, 160, 160,
#                      fill='green')

game = GameSnake(0, -20)
go()

c.bind('<Up>',
       lambda event: game.goUp())
c.bind('<Down>',
       lambda event: game.goDown())
c.bind('<Left>',
       lambda event: game.goLeft())
c.bind('<Right>',
       lambda event: game.goRight())
#

root.mainloop()

