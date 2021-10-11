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

def goUp():
    if game.y > 0:
        return
    game.x = 0
    game.y = -30

def goDown():
    if game.y < 0:
        return
    game.x = 0
    game.y = 30

def goLeft():
    if game.x > 0:
        return
    game.x = -30
    game.y = 0

def goRight():
    if game.x < 0:
        return
    game.x = 30
    game.y = 0

snake = c.create_rectangle(400, 400, 430, 430, fill='green')
# ball = c.create_oval(40, 140, 160, 160,
#                      fill='green')

game = GameSnake(0, -20)
go()

c.bind('<Up>',
       lambda event: goUp())
c.bind('<Down>',
       lambda event: goDown())
c.bind('<Left>',
       lambda event: goLeft())
c.bind('<Right>',
       lambda event: goRight())
#

root.mainloop()

