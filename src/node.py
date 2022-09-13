
class Node:
    def __init__(self) -> None:
        self.alive: bool = False
        self.is_dying = False
        self.spawning = False

    def bring_to_life(self) -> None:
        self.alive = True
        self.is_dying = False
        self.spawning = False

    def kill(self) -> None:
        self.alive = False
        self.is_dying = False
        self.spawning = False

    def set_as_dying(self):
        self.is_dying = True
        self.spawning = False

    def set_as_spawning(self):
        self.spawning = True
        self.is_dying = False
