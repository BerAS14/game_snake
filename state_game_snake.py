class StateGameSnake(object):
    def __init__(self):
        self.field = []
        self.snake = []
        self.direction = ''
        self.game_started = False
        self.count_step = 0
        self.game_over = True

    def __repr__(self):
        return str(vars(self))
