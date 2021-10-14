import unittest
from controller_game_snake import ControllerGameSnake
from drawing_graphics import transform_coordinate


def fun(x):
    return x + 1


class MyTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(4, fun(3))

    def test_snake(self):
        game = ControllerGameSnake()
        self.assertEqual(6, game.snake_head_x)
        self.assertEqual(4, game.snake_head_y)

    def test_go_up_from_start(self):
        game = ControllerGameSnake()
        game.go_up()
        self.assertEqual('Up', game.state.direction)

    def test_go_up_when_going_down(self):
        game = ControllerGameSnake()
        game.go_down()
        game.go_up()
        self.assertEqual('Down', game.state.direction)

    def test_go_up_when_going_left(self):
        game = ControllerGameSnake()
        game.go_left()
        game.go_up()
        self.assertEqual('Up', game.state.direction)

    def test_get_center(self):
        game = ControllerGameSnake()
        x = game.get_center()
        self.assertEqual((6, 4), x)

    def test_transformation_coordinate_0_9(self):
        x, y = transform_coordinate(0, 9, 13, 9)
        self.assertEqual((0, 0), (x, y))

    def test_transformation_coordinate_13_9(self):
        x, y = transform_coordinate(13, 9, 13, 9)
        self.assertEqual((1000, 0), (x, y))

    def test_transformation_coordinate_13_0(self):
        x, y = transform_coordinate(13, 0, 13, 9)
        self.assertEqual((1000, 700), (x, y))

    def test_game_do_step_up(self):
        game = ControllerGameSnake()
        game.game_init()
        game.state.game_started = True
        game.go_up()
        game.do_step()
        self.assertEqual("[{'x': 6, 'y': 5}, {'x': 6, 'y': 4}, {'x': 5, 'y': 4}, {'x': 4, 'y': 4}, {'x': 3, 'y': 4}]",
                         str(game.state.snake))

    def test_game_do_step_down(self):
        game = ControllerGameSnake()
        game.game_init()
        game.state.game_started = True
        game.go_down()
        game.do_step()
        self.assertEqual(
            "[{'x': 6, 'y': 3}, {'x': 6, 'y': 4}, {'x': 5, 'y': 4}, {'x': 4, 'y': 4}, {'x': 3, 'y': 4}]",
            str(game.state.snake))

    def test_game_do_step_right(self):
        game = ControllerGameSnake()
        game.game_init()
        game.state.game_started = True
        game.go_right()
        game.do_step()
        self.assertEqual(
            "[{'x': 5, 'y': 4}, {'x': 6, 'y': 4}, {'x': 5, 'y': 4}, {'x': 4, 'y': 4}, {'x': 3, 'y': 4}]",
            str(game.state.snake))

    def test_game_do_step_right(self):
        game = ControllerGameSnake()
        game.game_init()
        game.state.game_started = True
        game.go_down()
        game.go_right()
        game.do_step()
        self.assertEqual(
            "[{'x': 7, 'y': 4}, {'x': 6, 'y': 4}, {'x': 5, 'y': 4}, {'x': 4, 'y': 4}, {'x': 3, 'y': 4}]",
            str(game.state.snake))
