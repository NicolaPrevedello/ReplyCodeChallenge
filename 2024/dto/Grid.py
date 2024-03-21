import numpy as np

from GoldenPoints import GoldenPoint

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.empty((height, width), dtype=object)

    def __str__(self):
        return f"Grid: Width={self.width}, Height={self.height}"

    def set_tile(self, x, y, tile):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = tile
        else:
            print("Error: Coordinates out of grid bounds.")

    def get_tile(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        else:
            print("Error: Coordinates out of grid bounds.")
            return None
        
    def point_distance(x1:int, y1:int, x2:int, y2:int) -> int:
        distance = abs(x2 - x1) + abs(y2 - y1)
        return distance
        
