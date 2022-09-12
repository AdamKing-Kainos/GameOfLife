import pytest
from src.node import Node


def test_when_new_cell_created_it_is_dead():
    cell = Node()
    assert cell.alive is False

def test_bring_to_life_sets_cell_to_alive():
    cell = Node()
    cell.bring_to_life()
    assert cell.alive is True

def test_kill_sets_cell_to_dead():
    cell = Node()
    cell.bring_to_life()
    cell.kill()
    assert cell.alive is False
