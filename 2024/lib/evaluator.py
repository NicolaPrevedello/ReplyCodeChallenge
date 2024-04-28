import input_parser as ip
import output_parser as op


def evaluate(input_file, output_file):

    #PARSING DEL FILE DI INPUT
    num_cols, num_rows, num_golden_points, num_silver_points, num_tile_types, golden_points, silver_points, tiles = ip.parse_input_file(input_file)

    #PARSING DEL FILE DI OUTPUT
    tile_data = op.parse_output_file(output_file)

    score = 0 

    for point in silver_points:
        x1, y1, score1 = point
        for tile in tile_data:
            id, x, y = tile
            if (x1==x & y1==y):
                score += score1

    for tile in tile_data:
        id, x, y = tile
        score -= tiles.get(id)['cost']


    return score

input_file_path = './2024/data/00-trailer.txt'
output_file_path = './2024/output/00-trailer_Solution1.txt'
score = evaluate (input_file_path, output_file_path)

print('Il punteggio è : ', score)


#QUESTO NON è L'EVALUATOR CORRETTO, RILEGGI IL TESTO DEL PROBLEMA