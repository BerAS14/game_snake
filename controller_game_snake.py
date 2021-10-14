from state_game_snake import StateGameSnake
from point import Point


class ControllerGameSnake(object):
    def __init__(self):
        self.state = StateGameSnake()
        self.state.field = [13, 9, 'white']
        self.snake_head_x, self.snake_head_y = self.get_center()

    def __repr__(self):
        return str(vars(self))

    def get_center(self):
        x_center = self.state.field[0] // 2
        y_center = self.state.field[1] // 2
        return x_center, y_center

    def start(self):
        self.state.game_started = True

    def do_step(self):
        if not self.state.game_started:
            return
        if self.state.direction == 'Up':
            self.state.snake.pop()
            head_point = self.state.snake[0]
            self.state.snake.insert(0, Point(head_point.x, head_point.y + 1))
        if self.state.direction == 'Down':
            self.state.snake.pop()
            head_point = self.state.snake[0]
            self.state.snake.insert(0, Point(head_point.x, head_point.y - 1))
        if self.state.direction == 'Left':
            self.state.snake.pop()
            head_point = self.state.snake[0]
            self.state.snake.insert(0, Point(head_point.x - 1, head_point.y))
        if self.state.direction == 'Right':
            self.state.snake.pop()
            head_point = self.state.snake[0]
            self.state.snake.insert(0, Point(head_point.x + 1, head_point.y))
        self.state.count_step += 1

    def game_init(self):

        self.state.snake = []
        for i in range(5):
            self.state.snake.append(Point(self.snake_head_x - i, self.snake_head_y))
        self.state.direction = 'Right'
        self.state.count_step = 0
        self.state.game_over = False

    def go_up(self):
        if self.state.direction == 'Down':
            return
        self.state.direction = 'Up'

    def go_down(self):
        if self.state.direction == 'Up':
            return
        self.state.direction = 'Down'

    def go_left(self):
        if self.state.direction == 'Right':
            return
        self.state.direction = 'Left'

    def go_right(self):
        if self.state.direction == 'Left':
            return
        self.state.direction = 'Right'

