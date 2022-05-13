import pyxel

class Fruit:
    def __init__(self):
        self.x = 5 * pyxel.rndi(8,22)
        self.y = 5 * pyxel.rndi(8,22)

    def draw(self):
        pyxel.rect(self.x,self.y,5,5,7)