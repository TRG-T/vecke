from direction import Direction
from tail import Tail
import pyxel

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