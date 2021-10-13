import pprint
import unittest

import gameSnake
from Example import transformation_coordinate
from gameSnake import GameSnake


def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(4, fun(3))

    def test_snake(self):
        game = GameSnake()
        self.assertEqual(6, game.snake_head_x)
        self.assertEqual(4, game.snake_head_y)

    def test_go_up_from_start(self):
        game = GameSnake()
        game.goUp()
        self.assertEqual('Up', game.condition.direction)

    def test_go_up_when_going_down(self):
        game = GameSnake()
        game.goDown()
        game.goUp()
        self.assertEqual('Down', game.condition.direction)

    def test_go_up_when_going_left(self):
        game = GameSnake()
        game.goLeft()
        game.goUp()
        self.assertEqual('Up', game.condition.direction)
    
    def test_game_start(self):
        new_game = GameSnake()
        new_game.game_start()
        print(new_game)

    def test_get_center(self):
        game = GameSnake()
        x = game.get_center()
        self.assertEqual((6, 4), x)

    def test_transformation_coordinate_0_9(self):
        game = GameSnake()
        x, y = transformation_coordinate(game, 0, 9)
        self.assertEqual((0, 0), (x, y))

    def test_transformation_coordinate_13_9(self):
        game = GameSnake()
        x, y = transformation_coordinate(game, 13, 9)
        self.assertEqual((700, 0), (x, y))

    def test_transformation_coordinate_13_0(self):
        game = GameSnake()
        x, y = transformation_coordinate(game, 13, 0)
        self.assertEqual((700, 500), (x, y))
