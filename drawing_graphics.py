from tkinter import Canvas, Tk
from controller_game_snake import ControllerGameSnake


def transform_coordinate(x, y, state_field_width, state_field_height):
    return round(DrawingGraphics.screen_field_width / state_field_width * x), round(
        DrawingGraphics.screen_field_height - y * DrawingGraphics.screen_field_height / state_field_height)


class DrawingGraphics(object):
    screen_field_width = 1000
    screen_field_height = 700
    color_field = 'white'
    color_head_snake = 'blue'
    color_snake = 'green'

    def __init__(self):

        root = Tk()
        self.c = Canvas(width=DrawingGraphics.screen_field_width, height=DrawingGraphics.screen_field_height,
                        bg=DrawingGraphics.color_field)
        self.c.focus_set()
        self.c.pack()
        self.controller = ControllerGameSnake()
        self.controller.game_init()
        self.snake = []
        for i, point in enumerate(self.controller.state.snake):

            screen_x, screen_y = transform_coordinate(point.x, point.y, self.controller.state.field[0], self.controller.state.field[1])
            screen_width, screen_height = self.get_size_rectangle()
            color = DrawingGraphics.color_snake if i > 0 else DrawingGraphics.color_head_snake
            self.snake.append(self.c.create_rectangle(screen_x, screen_y, screen_x + screen_width, screen_y + screen_height, fill=color))

        self.go()
        self.c.bind('<KeyRelease-space>',
                    lambda event: self.controller.start())
        self.c.bind('<Up>',
                    lambda event: self.controller.go_up())
        self.c.bind('<Down>',
                    lambda event: self.controller.go_down())
        self.c.bind('<Left>',
                    lambda event: self.controller.go_left())
        self.c.bind('<Right>',
                    lambda event: self.controller.go_right())
        root.mainloop()

    def go(self):
        self.controller.do_step()
        i = 0
        for j in self.controller.state.snake:
            x, y = transform_coordinate(j.x, j.y, self.controller.state.field[0], self.controller.state.field[1])
            screen_width, screen_height = self.get_size_rectangle()
            self.c.coords(self.snake[i], x, y, x + screen_width, y + screen_height)
            i += 1
        self.c.after(200, self.go)

    def get_size_rectangle(self):
        return round(DrawingGraphics.screen_field_width / self.controller.state.field[0] * 1), round(
            1 * DrawingGraphics.screen_field_height / self.controller.state.field[1])

