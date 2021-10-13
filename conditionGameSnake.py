from point import Point

class ConditionGameSnake(object):


    def __init__(self):
        self.field = []
        self.snake = []
        self.direction = ''
        self.game_started = False

    def __repr__(self):
        return str(vars(self))

