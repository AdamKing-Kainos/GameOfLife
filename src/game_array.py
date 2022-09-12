from src.node import Node

class GameArray:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.array = [[Node() for cell in range(width)] for row in range(height)]

    def within_array(self, x_position: int, y_position: int) -> bool:
        is_within_array = True
        if x_position < 0 or x_position >= self.width:
            is_within_array = False
        elif y_position < 0 or y_position >= self.height:
            is_within_array = False

        return is_within_array

    def alive_neighbours(self, x_position: int, y_position: int) -> int:
        alive_neighbours = 0
        neighbours: list[tuple[int,int]]= [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
        for neighbour in neighbours:
            a, b = neighbour
            x = x_position + a
            y = y_position + b
            if self.within_array(x,y):
                if self.array[x][y].alive:
                    alive_neighbours += 1
        return alive_neighbours
