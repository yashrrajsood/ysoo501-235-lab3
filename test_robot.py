import pytest

from robot import Robot, Direction, IllegalMoveException


@pytest.fixture
def robot():
    return Robot()


def test_constructor(robot):
    state = robot.state()

    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1


def test_east_turn(robot):
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.EAST


def test_west_turn(robot):
    robot.turn()
    robot.turn()
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.WEST


def test_south_turn(robot):
    robot.turn()
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.SOUTH


def test_north_turn(robot):
    robot.turn()
    robot.turn()
    robot.turn()
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.NORTH


def test_illegal_move_south(robot):
    robot.turn();
    robot.turn();

    with pytest.raises(IllegalMoveException):
        robot.move()


def test_illegal_move_north(robot):
    for x in range(9):
        robot.move()
    with pytest.raises(IllegalMoveException):
        robot.move()


def test_illegal_move_east(robot):
    robot.turn()
    for x in range(9):
        robot.move()
    with pytest.raises(IllegalMoveException):
        robot.move()


def test_illegal_move_west(robot):
    robot.turn()
    robot.turn()
    robot.turn()
    with pytest.raises(IllegalMoveException):
        robot.move()


def test_move_north(robot):
    robot.move()
    state = robot.state()
    assert state['row'] == 9
    assert state['col'] == 1


def test_move_east(robot):
    robot.turn()
    robot.move()
    state = robot.state()
    assert state['row'] == 10
    assert state['col'] == 2


def test_move_south(robot):
    robot.move()
    robot.turn()
    robot.turn()
    robot.move()

    state = robot.state()
    assert state['row'] == 10
    assert state['col'] == 1


def test_move_west(robot):
    robot.turn()
    robot.move()

    robot.turn()
    robot.turn()
    robot.move()

    state = robot.state()
    assert state['row'] == 10
    assert state['col'] == 1


def test_back_track_without_history(robot):
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1


def test_back_track_with_move(robot):
    robot.move()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1


def test_back_track_with_turn(robot):
    robot.turn()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1


def test_back_track_once_with_multiple_moves(robot):
    robot.move()
    robot.move()
    robot.move()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 8
    assert state['col'] == 1


def test_back_track_all_with_multiple_moves(robot):
    robot.move()
    robot.move()
    robot.move()
    robot.back_track()
    robot.back_track()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1