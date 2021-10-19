from state_game_snake import StateGameSnake
from point import Point


class ControllerGameSnake(object):
    def __init__(self):
        self.state = StateGameSnake()
        self.state.field = [23, 17, 'white']


    def __repr__(self):
        return str(vars(self))

    def get_center(self):
        x_center = self.state.field[0] // 2
        y_center = self.state.field[1] // 2
        return x_center, y_center

    def start(self):
        self.state.game_started = True

    def do_step(self):
        if self.state.game_over:
            return
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
        self.state.step_over = True
        self.game_over()

    def game_init(self):
        snake_head_x, snake_head_y = self.get_center()
        self.state.snake = []
        for i in range(5):
            self.state.snake.append(Point(snake_head_x - i, snake_head_y))
        self.state.direction = 'Right'
        self.state.step_over = False
        self.state.game_over = False

    def go_up(self):
        if self.state.direction == 'Down' or not self.state.step_over:
            return
        self.state.direction = 'Up'
        self.state.step_over = False

    def go_down(self):
        if self.state.direction == 'Up' or not self.state.step_over:
            return
        self.state.direction = 'Down'
        self.state.step_over = False

    def go_left(self):
        if self.state.direction == 'Right' or not self.state.step_over:
            return
        self.state.direction = 'Left'
        self.state.step_over = False

    def go_right(self):
        if self.state.direction == 'Left' or not self.state.step_over:
            return
        self.state.direction = 'Right'
        self.state.step_over = False

    @property
    def head_x(self):
        return self.state.snake[0].x

    @property
    def head_y(self):
        return self.state.snake[0].y

    @property
    def state_width(self):
        return self.state.field[0]

    @property
    def state_height(self):
        return self.state.field[1]

    def game_over(self):
        # странное поведение, нужно разобраться
        if not 0 <= self.head_x <= self.state_width-1:
            self.state.game_over = True
        if not 0 < self.head_y <= self.state_height:
            self.state.game_over = True


