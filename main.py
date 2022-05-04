import pyxel

class Fruit:
    def __init__(self):
        self.x = 5 * pyxel.rndi(8,22)
        self.y = 5 * pyxel.rndi(8,22)

    def draw(self):
        pyxel.rect(self.x,self.y,5,5,7)


class Character:
    def __init__(self):
        self.x = 75
        self.y = 75
        self.direction = None
        self.points = 0

    def up(self):
        self.direction = "up"

    def right(self):
        self.direction = "right"

    def down(self):
        self.direction = "down"

    def left(self):
        self.direction = "left"

    def point(self):
        self.points += 1


    def update(self):
        #print(f"x: {self.x}, y: {self.y}")
        match self.direction:
            case "up":
                self.y  = max(self.y - 5, 0)
            case "right":
                self.x = max(self.x + 5, 0)
            case "down":
                self.y = max(self.y + 5, 0)
            case "left":
                self.x = max(self.x - 5, 0)
            case _:
                self.x = self.x

        if self.x > 115:
            self.x = 40
        elif self.x < 40:
            self.x = 115


        if self.y > 115:
            self.y = 40
        elif self.y < 40:
            self.y = 115

    def draw(self):
        self.update()
        pyxel.rect(self.x,self.y,5,5,8)

class Game:
    def __init__(self):
        pyxel.init(100,100, "Vectoar", 12, pyxel.KEY_Q)
        pyxel.camera(30,30)
        pyxel.rseed(4)
        self.character = Character()
        self.fruit = Fruit()
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_W):
            self.character.up()
        elif pyxel.btnp(pyxel.KEY_D):
            self.character.right()
        elif pyxel.btnp(pyxel.KEY_S):
            self.character.down()
        elif pyxel.btnp(pyxel.KEY_A):
            self.character.left()
        
        if self.fruit.x == self.character.x and self.fruit.y == self.character.y:
            self.fruit = Fruit()
            self.character.point()
            
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(40,40,80,80,1)
        pyxel.text(115,33, str(self.character.points), 13)
        self.fruit.draw()
        self.character.draw()

Game()