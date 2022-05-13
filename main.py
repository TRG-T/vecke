import pyxel
import random
from time import time
from fruit import Fruit
from character import Character

random.seed(time())

class Game:
    def __init__(self):
        pyxel.init(100,100, "Snake game", 12, pyxel.KEY_Q)
        pyxel.camera(30,30)
        pyxel.rseed(random.randint(0,100))
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
            self.character.grow()

            
    def draw(self):
        if not self.character.lost:
            pyxel.cls(0)
            pyxel.rect(40,40,80,80,1)
            pyxel.text(115,33, str(self.character.score), 7)
            self.fruit.draw()
            self.character.draw()
        else:
            pyxel.rect(0,0,150,150,0)
            pyxel.text(65,65, "you lost", 7)
            pyxel.text(65,75, "score: {score}".format(score = self.character.score), 7)
            pyxel.text(62,85, "r to reset", 7)

Game()