import pyxel

class Character:
    def __init__(self):
        self.x = 30
        self.y = 30
        self.direction = None

    def up(self):
        self.direction = "up"

    def right(self):
        self.direction = "right"

    def down(self):
        self.direction = "down"

    def left(self):
        self.direction = "left"

    def update(self):
        match self.direction:
            case "up":
                self.y  = max(self.y - 10, 0)
            case "right":
                self.x = max(self.x + 10, 0)
            case "down":
                self.y = max(self.y + 10, 0)
            case "left":
                self.x = max(self.x - 10, 0)
            case _:
                self.x = self.x

        if self.x > pyxel.width+30:
            self.x = 30
        elif self.x < 30:
            self.x = pyxel.width+30


        if self.y > pyxel.height+30:
            self.y = 30
        elif self.y < 30:
            self.y = pyxel.height+30

    def draw(self):
        self.update()
        pyxel.rect(self.x,self.y,8,8,8)

class Game:
    def __init__(self):
        pyxel.init(100,100, "Vectoar", 15, pyxel.KEY_Q)
        pyxel.camera(30,30)
        self.character = Character()
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
            
    def draw(self):
        pyxel.cls(0)
        self.character.draw()

Game()