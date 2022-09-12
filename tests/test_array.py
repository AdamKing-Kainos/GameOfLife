import pytest

from src.node import Node
from src.game_array import GameArray


def test_when_given_make_1x1_make_array_returns_a_1x1_array():
    array = GameArray(1,1)
    assert len(array.array) == 1
    assert len(array.array[0]) == 1

def test_make_array_returns_an_array_of_Nodes():
    array = GameArray(1, 1)
    for row in array.array:
        for cell in row:
            assert isinstance(cell, Node)

def test_when_given_height_and_width_make_array_returns_a_height_and_width_array():
    array = GameArray(10, 10)
    assert len(array.array) == 10
    assert len(array.array[0]) == 10

def test_when_requested_a_dead_cell_in_an_array_can_be_made_alive():
    array = GameArray(10, 10)
    array.array[3][3].bring_to_life()
    assert array.array[3][3].alive is True

def test_when_requested_a_alive_cell_in_an_array_can_be_made_dead():
    array = GameArray(10, 10)
    array.array[3][3].bring_to_life()
    array.array[3][3].kill()
    assert array.array[3][3].alive is False


def test_given_a_postion_outside_of_an_array_within_array_returns_true():
    array = GameArray(3, 3)
    assert array.within_array(1,1) is True


def test_given_a_postion_outside_of_an_array_within_array_returns_false():
    array = GameArray(3, 3)
    assert array.within_array(1,4) is False
    assert array.within_array(4,1) is False


def test_any_node_in_the_array_can_count_the_number_of_alive_neighbours_it_has():
    array = GameArray(3, 3)
    array.array[0][1].bring_to_life()
    array.array[1][0].bring_to_life()
    array.array[1][2].bring_to_life()
    array.array[2][1].bring_to_life()
    assert array.alive_neighbours(1,1) == 4