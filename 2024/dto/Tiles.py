class Tile:
    def __init__(self, tile_id, cost, count, up: bool, down: bool, right: bool, left: bool):
        self.tile_id = tile_id
        self.cost = cost
        self.count = count
        self.up = up
        self.down = down
        self.right = right
        self.left = left
    

    def __str__(self):
        return f"Tile ID: {self.tile_id}, Cost: {self.cost}, Count: {self.count}"