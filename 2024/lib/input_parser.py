def parse_input_file(filename):
  """
  Funzione che parsa il file di testo e restituisce i dati estratti.

  Args:
    filename: Il nome del file di testo da parsare.

  Returns:
    Una tupla contenente:
      - num_cols: Numero di colonne della matrice.
      - num_rows: Numero di righe della matrice.
      - num_golden_points: Numero di golden points.
      - num_silver_points: Numero di silver points.
      - num_tile_types: Numero di tipologie di tiles consentiti.
      - golden_points: Lista di coordinate (x, y) dei golden points.
      - silver_points: Lista di coordinate (x, y, score) dei silver points.
      - tiles: Lista di dizionari contenenti le informazioni sui tiles:
          - id: Identificativo del tile.
          - cost: Costo del tile.
          - availability: Disponibilità del tile.
  """

  with open(filename, 'r') as f:
    # Prima riga: dati della matrice, golden points, silver points e tile types
    line = f.readline().strip()
    num_cols, num_rows, num_golden_points, num_silver_points, num_tile_types = map(int, line.split())

    # Lista di golden points
    golden_points = []
    for _ in range(num_golden_points):
      line = f.readline().strip()
      x, y = map(int, line.split())
      golden_points.append((x, y))

    # Lista di silver points
    silver_points = []
    for _ in range(num_silver_points):
      line = f.readline().strip()
      x, y, score = map(int, line.split())
      silver_points.append((x, y, score))

    # Lista di tiles
    tiles = []
    for _ in range(num_tile_types):
      line = f.readline().strip()
      tile_id, cost, availability = line.split()
      tiles.append({
          'id': tile_id,
          'cost': int(cost),
          'availability': int(availability)
      })

  return (num_cols, num_rows, num_golden_points, num_silver_points, num_tile_types,
          golden_points, silver_points, tiles)
