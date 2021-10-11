class GameSnake(object):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        
    def goUp(self):
        if self.y > 0:
            return
        self.x = 0
        self.y = -30
    
    def goDown(self):
        if self.y < 0:
            return
        self.x = 0
        self.y = 30
    
    def goLeft(self):
        if self.x > 0:
            return
        self.x = -30
        self.y = 0
    
    def goRight(self):
        if self.x < 0:
            return
        self.x = 30
        self.y = 0

if __name__ == "__main__":
    game = GameSnake('Up')
    # print(self.directionMovement)

