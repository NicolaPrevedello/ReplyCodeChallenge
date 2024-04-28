def parse_output_file(filename):
    """
    Parses a text file containing tile ID and coordinate information.

    Args:
        filename (str): Path to the text file.

    Returns:
        list: A list of lists, where each inner list represents a tile
            with its ID, coordinates, and potentially other information.
    """

    tile_data = []

    with open(filename, 'r') as f:
        for line in f:
            # Split the line into tile ID, x-coordinate, and y-coordinate
            tile_id, x, y = line.strip().split()

            # Convert x and y to integers
            x, y = int(x), int(y)

            # Create a list for each tile and append to the main list
            tile_info = [tile_id, x, y]
            tile_data.append(tile_info)

    return tile_data
