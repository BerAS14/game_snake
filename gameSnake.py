from conditionGameSnake import ConditionGameSnake
from point import Point


class GameSnake(object):
    def __init__(self):
        self.condition = ConditionGameSnake()
        self.condition.field = [13, 9, 'white']
        self.snake_head_x, self.snake_head_y = self.get_center()


    def __repr__(self):
        return str(vars(self))

    def get_center(self):
        x_center = self.condition.field[0] // 2
        y_center = self.condition.field[1] // 2
        return x_center, y_center



    def game_start(self):

        self.condition.snake = []
        for i in range(5):
            self.condition.snake.append(Point(self.snake_head_x - i, self.snake_head_y))
        self.condition.direction = 'Left'
        self.condition.game_started = True

    def goUp(self):
        if self.condition.direction == 'Down':
            return
        self.condition.direction = 'Up'
        # self.snake_head_x = 0
        # self.snake_head_y = -30
    
    def goDown(self):
        if self.condition.direction == 'Up':
            return
        self.condition.direction = 'Down'
        # self.snake_head_x = 0
        # self.snake_head_y = 30
    
    def goLeft(self):
        if self.condition.direction == 'Right':
            return
        self.condition.direction = 'Left'
        # self.snake_head_x = -30
        # self.snake_head_y = 0
    
    def goRight(self):
        if self.condition.direction == 'Left':
            return
        self.condition.direction = 'Right'
        # self.snake_head_x = 30
        # self.snake_head_y = 0

if __name__ == "__main__":
    # game = GameSnake('Up')
    GameSnake().game_start()
