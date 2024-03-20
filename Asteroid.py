from NPO import NonPlayerObject
import random
import arcade
import math
import parameters
from Drop import Drop

class Asteroid(NonPlayerObject):
    def setRotation(self):
        self.rotationSpeed = random.randint(-10,10)

    def update(self):
        self.angle += self.rotationSpeed
        super().update()

    def setSize(self, size):
        self.health = math.ceil(size/3)
        self.size = size
        self.shieldCurrent = 0

    def kill(self):
        drop_list = arcade.SpriteList()
        child_list = arcade.SpriteList()
        num = math.ceil(self.size/2)
        for i in range(num):
            drop = Drop("sprites/drops/01.png", 1)
            drop.setup(1, self.center_x+random.randint(-parameters.SCREEN_WIDTH/50, parameters.SCREEN_WIDTH/50), self.center_y+random.randint(-parameters.SCREEN_HEIGHT/50, parameters.SCREEN_HEIGHT/50))
            drop_list.append(drop)
        for i in range(1, num):
            child = Asteroid("sprites/asset/meteor.png", parameters.SCALING*(i-1)/2)
            child.setSize(i-1)
            child.setRotation()
            child.center_x = self.center_x
            child.center_y = self.center_y
            child.velocity = (random.randint(-3,3), random.randint(-3,3))
            child_list.append(child)
        self.remove_from_sprite_lists()
        return (drop_list, child_list)

    def hit(self, damage):
        self.health -= damage
