import pyxel
from enum import Enum
import random
from time import time

random.seed(time())

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Fruit:
    def __init__(self):
        self.x = 5 * pyxel.rndi(8,22)
        self.y = 5 * pyxel.rndi(8,22)

    def draw(self):
        pyxel.rect(self.x,self.y,5,5,7)

class Tail:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Character:
    def __init__(self):
        self.x = 75
        self.y = 75
        self.direction = None
        self.score = 0
        self.tail = [1]
        self.lost = False

    def up(self):
        self.direction = Direction.UP

    def right(self):
        self.direction = Direction.RIGHT

    def down(self):
        self.direction = Direction.DOWN

    def left(self):
        self.direction = Direction.LEFT

    def grow(self):
        self.score += 1
        self.tail.append(Tail(self.x, self.y))

    def update_tail(self):
        for i in range(len(self.tail)-1, 0, -1):
            self.tail[i] = self.tail[i-1]

    def check_collision(self):
        for i in range(1, len(self.tail)):
            if self.tail[i].x == self.x and self.tail[i].y == self.y:
                self.lost = True

    def update(self):
        self.tail[0] = Tail(self.x, self.y)

        match self.direction:
            case Direction.UP:
                self.y  = max(self.y - 5, 0)
            case Direction.RIGHT:
                self.x = max(self.x + 5, 0)
            case Direction.DOWN:
                self.y = max(self.y + 5, 0)
            case Direction.LEFT:
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
        
        self.update_tail()
        self.check_collision()

    def draw(self):
        self.update()
        for i in range(1, len(self.tail)):
            pyxel.rect(self.tail[i].x,self.tail[i].y,5,5,8)
        pyxel.rect(self.x,self.y,5,5,8)

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