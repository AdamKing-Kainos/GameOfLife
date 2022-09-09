import pytest
from src.node import Node


def test_when_new_cell_created_it_is_dead():
    cell = Node()
    assert cell.alive == False

def test_bring_to_life_sets_cell_to_alive():
    cell = Node()
    cell.bring_to_life()
    assert cell.alive == True
