class Tile:
    def __init__(self, tile_id, cost, count):
        self.tile_id = tile_id
        self.cost = cost
        self.count = count
        self.paths = []


        if tile_id == '3':
            self.paths.append('left','right')
        if tile_id == '5':
            self.paths.append('down','right')
        if tile_id == '6':
            self.paths.append('left','down')
        if tile_id == '7':
            self.paths.append('left','right')
            self.paths.append('left','down')
            self.paths.append('down','right')
        if tile_id == '9':
            self.paths.append('up','right')   
        if tile_id == '96':
            self.paths.append('left','down')
            self.paths.append('up','right')
        if tile_id == 'A':
            self.paths.append('left','up')
        if tile_id == 'A5':
            self.paths.append('left','up')   
            self.paths.append('down','right')  
        if tile_id == 'B':
            self.paths.append('left','right')  
            self.paths.append('left','up') 
            self.paths.append('up','right')
        if tile_id == 'C': 
            self.paths.append('up','down')   
        if tile_id == 'C3':
            self.paths.append('left','right') 
            self.paths.append('up','down') 
        if tile_id == 'D':
            self.paths.append('up','down')
            self.paths.append('up','right')
            self.paths.append('down','right')
        if tile_id == 'E':
            self.paths.append('left','up')
            self.paths.append('left','down')
            self.paths.append('up','down')  
        if tile_id == "F":
            self.paths.append('left','right')
            self.paths.append('left','down')
            self.paths.append('left','up')  
            self.paths.append('up','down')
            self.paths.append('down','right')
            self.paths.append('up','right')  



    def __str__(self):
        return f"Tile ID: {self.tile_id}, Cost: {self.cost}, Count: {self.count}"