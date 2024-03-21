

from dto.Grid import Grid
from dto.Tiles import Tile

def parse_input_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Parse the first row containing grid dimensions and counts
    W, H, GN, SM, TL = map(int, lines[0].strip().split())

    grid = Grid(W,H)

    # Parse Golden Points
    golden_points = []
    for line in lines[1:GN+1]:
        x, y = map(int, line.strip().split())
        golden_points.append((x, y))
        grid.set_tile(x, y, "G")


    # Parse Silver Points
    silver_points = []
    for line in lines[GN+1:GN+SM+1]:
        x, y, score = map(int, line.strip().split())
        silver_points.append((x, y, score))
        grid.set_tile(x, y, "S"+score)


    # Parse Tiles
    tiles = set()
    for line in lines[GN+SM+1:]:
        tile_id, cost, count = line.strip().split()
        tiles.append(Tile(tile_id, cost, count)(tile_id, int(cost), int(count)))
    

    # return W, H, GN, SM, TL, golden_points, silver_points, tiles
    return grid

# Example usage:
filename = 'input.txt'  # Replace 'input.txt' with the actual filename
W, H, GN, SM, TL, golden_points, silver_points, tiles = parse_input_file(filename)
print("Width:", W)
print("Height:", H)
print("Number of Golden Points:", GN)
print("Number of Silver Points:", SM)
print("Number of Tile types:", TL)
print("Golden Points:", golden_points)
print("Silver Points:", silver_points)
print("Tiles:", tiles)