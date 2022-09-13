from src.node import Node


def test_when_new_cell_created_it_is_dead():
    cell = Node()
    assert cell.alive is False


def test_bring_to_life_sets_cell_to_alive():
    cell = Node()
    cell.bring_to_life()
    assert cell.alive is True
    assert cell.is_dying is False


def test_kill_sets_cell_to_dead():
    cell = Node()
    cell.bring_to_life()
    cell.kill()
    assert cell.alive is False


def test_which_will_die_next_generation_is_marked_as_dying():
    cell = Node()
    cell.bring_to_life()
    cell.set_as_dying()
    assert cell.is_dying is True


def test_dead_cell_which_resurrect_next_generation_is_marked_as_resurrect_equal_true():
    cell = Node()
    cell.set_as_spawning()
    assert cell.spawning is True


def test_bring_a_cell_back_to_life_sets_will_die_to_false():
    cell = Node()
    cell.bring_to_life()
    cell.set_as_dying()
    assert cell.alive is True
    assert cell.is_dying is True
    cell.kill()
    assert cell.alive is False
    cell.bring_to_life()
    assert cell.alive is True
    assert cell.is_dying is False


def test_a_spawning_cell_is_not_dying_in_the_same_iteration():
    cell = Node()
    cell.bring_to_life()
    cell.set_as_dying()
    cell.kill()
    cell.set_as_spawning()
    assert cell.is_dying is False


def test_a_dying_cell_is_not_spawning_in_the_same_iteration():
    cell = Node()
    cell.bring_to_life()
    cell.set_as_dying()
    cell.kill()
    cell.set_as_spawning()
    cell.bring_to_life()
    cell.set_as_dying()
    assert cell.spawning is False
