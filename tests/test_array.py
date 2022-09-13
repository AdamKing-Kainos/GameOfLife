from src.game_array import GameArray
from src.node import Node
from src.rule import Rule


def test_when_given_make_1x1_make_array_returns_a_1x1_array():
    array = GameArray(1, 1)
    assert len(array.array) == 1
    assert len(array.array[0]) == 1


def test_make_array_returns_an_array_of_nodes():
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


def test_given_a_position_outside_of_an_array_within_array_returns_true():
    array = GameArray(3, 3)
    assert array.within_array(1, 1) is True


def test_given_a_position_outside_of_an_array_within_array_returns_false():
    array = GameArray(3, 3)
    assert array.within_array(1, 4) is False
    assert array.within_array(4, 1) is False


def test_any_node_in_the_array_can_count_the_number_of_alive_neighbours_it_has():
    array = GameArray(3, 3)
    array.array[0][1].bring_to_life()
    array.array[1][0].bring_to_life()
    array.array[1][2].bring_to_life()
    array.array[2][1].bring_to_life()
    assert array.alive_neighbours(1, 1) == 4


def test_live_cell_with_less_than_two_alive_neighbours_sets_is_dying_to_true():
    rule = Rule(0, 1, True, 'kill',
                'Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.')
    print(rule)
    array = GameArray(3, 3)
    array.array[1][1].bring_to_life()
    array.array[0][1].bring_to_life()
    array.apply_rule(rule, 1, 1)
    assert array.alive_neighbours(1, 1) == 1
    assert array.array[1][1].alive is True
    assert array.array[1][1].is_dying is True
    assert array.array[1][1].spawning is False


def test_cell_with_more_than_3_alive_neighbours_sets_is_dying_to_true():
    rule = Rule(4, 8, True, 'kill',
                'Any live cell with more than three live neighbours dies, as if by overcrowding.')
    print(rule)
    array = GameArray(3, 3)
    array.array[1][1].bring_to_life()
    array.array[0][1].bring_to_life()
    array.array[1][0].bring_to_life()
    array.array[1][2].bring_to_life()
    array.array[2][1].bring_to_life()
    array.apply_rule(rule, 1, 1)
    assert array.alive_neighbours(1, 1) == 4
    assert array.array[1][1].alive is True
    assert array.array[1][1].is_dying is True
    assert array.array[1][1].spawning is False

def test_alive_cell_with_two_neighbours_maintains_state():
    rule = Rule(2, 3, True, 'maintain', 'Any live cell with two or three live neighbours lives on to the next generation')
    array = GameArray(3, 3)
    array.array[1][1].bring_to_life()
    array.array[0][1].bring_to_life()
    array.array[1][0].bring_to_life()
    array.apply_rule(rule, 1, 1)
    assert array.alive_neighbours(1, 1) == 2
    assert array.array[1][1].is_dying is False
    assert array.array[1][1].spawning is False
    assert array.array[1][1].alive is True


def test_alive_cell_with_3_neighbours_stays_alive():
    rule = Rule(2, 3, True, 'maintain', 'Any live cell with two or three live neighbours lives on to the next generation')
    array = GameArray(3, 3)
    array.array[1][1].bring_to_life()
    array.array[0][1].bring_to_life()
    array.array[1][0].bring_to_life()
    array.array[0][0].bring_to_life()
    array.apply_rule(rule, 1, 1)

    assert array.alive_neighbours(1, 1) == 3
    assert array.array[1][1].is_dying is False
    assert array.array[1][1].spawning is False
    assert array.array[1][1].alive is True

def test_dead_cell_with_3_alive_neighbours_becomesT_alive():
    rule = Rule(3, 3, False, 'spawn', 'Any dead cell with exactly three live neighbours becomes a live cell')
    array = GameArray(3, 3)
    array.array[0][1].bring_to_life()
    array.array[1][0].bring_to_life()
    array.array[0][0].bring_to_life()
    array.apply_rule(rule, 1, 1)
    assert array.alive_neighbours(1, 1) == 3
    assert array.array[1][1].is_dying is False
    assert array.array[1][1].spawning is True
    assert array.array[1][1].alive is False