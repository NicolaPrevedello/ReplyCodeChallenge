import input_parser as ip
import output_parser as op
from PIL import Image

def draw_solution(input_file, output_file, tile_pixel):

    #SETTING COLORE DI FONDO
    colore_sfondo = (255, 255, 255)

    #PARSING DEL FILE DI INPUT
    num_cols, num_rows, num_golden_points, num_silver_points, num_tile_types, golden_points, silver_points, tiles = ip.parse_input_file(input_file)

    #PARSING DEL FILE DI OUTPUT
    tile_data = op.parse_output_file(output_file)

    board = Image.new("RGBA", (num_cols*tile_pixel, num_rows*tile_pixel), colore_sfondo)

    #BASE PATH IMAGES
    basepath = "2024/images/Tiles/"

    # Define the tile dictionary
    tile_map = {}

    # Define the tile IDs
    tile_ids = ["3", "5", "6", "7", "9", "A", "B", "C", "D", "E", "F"]

    # Create and resize images, adding them to the dictionary
    for tile_id in tile_ids:
        # Construct the filename using basepath and tile_id
        filename = f"{basepath}Tile_{tile_id}.png"  # Assuming your filenames follow this format

        # Open and resize the image
        tile_map[tile_id] = Image.open(filename).resize((tile_pixel, tile_pixel))

    golden_point_tile = Image.open(f"{basepath}Golden_Point.png").resize((tile_pixel, tile_pixel))
    silver_point_tile = Image.open(f"{basepath}Silver_Point.png").resize((tile_pixel, tile_pixel))

    #DISEGNO I GOLDEN POINTS
    for point in golden_points:
        x, y = point  # Unpack the tuple
        #print(f"Point: (x={x}, y={y})")
        board.paste(golden_point_tile, (tile_pixel*x, tile_pixel*y), golden_point_tile)

    #DISEGNO I SILVER POINTS
    for point in silver_points:
        x, y, score = point  # Unpack the tuple
        #print(f"Point: (x={x}, y={y}), Score: {score}")
        board.paste(silver_point_tile, (tile_pixel*x, tile_pixel*y), silver_point_tile)

    #DISEGNO TILES DELLA SOLUZIONE
    for tile in tile_data:
        tile_id, x, y = tile
        #print(f"Tile: (id={tile_id}, x={x}, y={y})")
        board.paste(tile_map.get(tile_id), (tile_pixel*x, tile_pixel*y), tile_map.get(tile_id))

    board.show()

    return()


#TEST DRAW SOLUTION

input_file_path = './2024/data/02-sentimental.txt'
output_file_path = './2024/output/02-sentimental_out.txt'
tile_pixel = 50
draw_solution(input_file_path, output_file_path, tile_pixel)

