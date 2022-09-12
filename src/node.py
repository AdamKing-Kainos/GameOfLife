
class Node:
    def __init__(self) -> None:
        self.alive: bool = False

    def bring_to_life(self) -> None:
        self.alive = True

    def kill(self) -> None:
        self.alive = False
