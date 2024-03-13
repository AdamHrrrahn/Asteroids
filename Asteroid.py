from NPO import NonPlayerObject
import random
import arcade
class Asteroid(NonPlayerObject):
    def setRotation(self):
        self.rotationSpeed = random.randint(-10,10)
    def update(self):
        self.angle += self.rotationSpeed
        super().update()


