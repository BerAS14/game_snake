class Point(object):

    def __init__(self, x, y) -> None:
        super().__init__()
        self.x = x
        self.y = y

if __name__ == "__main__":
    pointHadSnake = Point(100, 100)
    print(pointHadSnake.x)
