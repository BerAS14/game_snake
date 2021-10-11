import unittest

from gameSnake import GameSnake


def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(4, fun(3))

    def test_snake(self):
        game = GameSnake(0, -20)
        self.assertEqual(0, game.x)
        self.assertEqual(-20, game.y)

    def test_go_up_from_start(self):
        game = GameSnake(0, 0)
        game.goUp()
        self.assertEqual((0, -30), (game.x, game.y))

    def test_go_up_when_going_down(self):
        game = GameSnake(0, 0)
        game.goDown()
        game.goUp()
        self.assertEqual((0, 30), (game.x, game.y))

    def test_go_up_when_going_left(self):
        game = GameSnake(0, 0)
        game.goLeft()
        game.goUp()
        self.assertEqual((0, -30), (game.x, game.y))
