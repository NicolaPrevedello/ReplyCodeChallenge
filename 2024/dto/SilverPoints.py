class SilverPoint:
    def __init__(self, x, y, score):
        self.x = x
        self.y = y
        self.score = score

    def __str__(self):
        return f"Silver Point - X: {self.x}, Y: {self.y}, Score: {self.score}"