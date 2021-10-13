from tkinter import Tk, Canvas

from gameSnake import GameSnake

def go():
    c.move(snake, game.snake_head_x, game.snake_head_y)
    c.after(100, go)

def transformation_coordinate(game, x, y):
    return round(700 / game.condition.field[0] * x), round(500 - y * 500 / game.condition.field[1])

if __name__ == "__main__":

    root = Tk()
    c = Canvas(width=700, height=500,
               bg='white')
    c.focus_set()
    c.pack()

    game = GameSnake()
    game.game_start()
    x, y = transformation_coordinate(game, game.snake_head_x, game.snake_head_y)
    snake = c.create_rectangle(x, y, x + 30, y + 30,  fill='green')

    c.bind('<KeyRelease-space>',
           lambda event: go())
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

