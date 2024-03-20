from NPO import NonPlayerObject
from Bullet import Bullet
from Drop import Drop
import math
import parameters
import arcade
import random

class EnemyShip(NonPlayerObject):
    def setup(self,center_x, center_y, velocity, angle):
        self.bulletSpeed = 10
        self.fireRate = 50
        self.cooldown = self.fireRate
        self.center_x = center_x
        self.center_y = center_y
        self.velocity = velocity
        self.angle = angle 
        self.maxTurn = 2
        self.turnChange = 0
        self.topSpeed = 3
        self.acceleration = 2
        self.bulletStrength = 1
        self.anamationSpeed = 10
        self.animationFrame = 0
        self.curTexture = 0
        self.straight_textures = []
        self.turn_left_textures = []
        self.turn_right_textures = []
        self.health = 2
        self.shieldMax = 1
        self.shieldCurrent = 1
        self.shieldCooldown = 600
        self.shieldRegen = 1


    def set_textures(self, textures):
        for i in range(0,4):
            self.straight_textures.append(textures[i])
        for i in range(6,9):
            self.turn_left_textures.append(textures[i])
        for i in range(9,12):
            self.turn_right_textures.append(textures[i])
        self.current_texture_list = self.straight_textures
        self.texture = self.current_texture_list[self.curTexture]

    def track(self, player_x, player_y):
        deltaX = player_x - self.center_x
        deltaY = player_y - self.center_y
        if (player_x < 0 or player_y < 0):
            self.turnChange = 0
            return
        targetAngle = math.degrees(math.atan2(deltaY, deltaX)) - 90
        if targetAngle > 0:
            targetAngle += 360
        self.turnChange = targetAngle - self.angle
        if self.turnChange > 180:
            self.turnChange -=360
        elif self.turnChange < -180:
            self.turnChange += 360
        if self.turnChange > self.maxTurn:
            self.turnChange = self.maxTurn
        elif self.turnChange < -self.maxTurn:
            self.turnChange = -self.maxTurn

    def change_animation(self, i):
        if i == 0:
            self.current_texture_list = self.straight_textures
        elif i == 1:
            self.current_texture_list = self.turn_left_textures
        elif i == 2:
            self.current_texture_list = self.turn_right_textures
        self.curTexture = self.curTexture % len(self.current_texture_list)
        self.texture = self.current_texture_list[self.curTexture]


    def update(self):
        if (self.shieldCurrent < self.shieldMax):
            self.shieldCooldown -= 1
            if self.shieldCooldown == 0:
                self.shieldCooldown = 600
                self.shieldCurrent += self.shieldRegen
                if self.shieldCurrent > self.shieldMax:
                    self.shieldCurrent = self.shieldMax

        self.angle += self.turnChange
        angleRad = math.radians(self.angle)
        deltaX, deltaY = self.velocity
        deltaX += -self.acceleration * math.sin(angleRad)
        deltaY += self.acceleration * math.cos(angleRad)
        speed = math.hypot(deltaX, deltaY)
        if speed > self.topSpeed:
            deltaX *= self.topSpeed/speed
            deltaY *= self.topSpeed/speed
        self.velocity = (deltaX, deltaY)
        if self.cooldown > 0:
            self.cooldown -= 1
        if self.turnChange == 0:
            self.change_animation(0)
        elif self.turnChange > 0:
            self.change_animation(1)
        elif self.turnChange < 0:
            self.change_animation(2)
        self.animationFrame += 1
        if (self.animationFrame == self.anamationSpeed):
            self.animationFrame = 0
            self.curTexture = (self.curTexture + 1) % len(self.current_texture_list)
            self.texture = self.current_texture_list[self.curTexture]
        super().update()

    def fire(self):
        self.cooldown = self.fireRate
        bullet = Bullet("sprites/asset/laser.png", parameters.SCALING)
        angleRad = math.radians(self.angle)
        x = -self.bulletSpeed * math.sin(angleRad)
        y = self.bulletSpeed * math.cos(angleRad)
        bullet.setup((x,y), self.center_x, self.center_y, self.angle, self.bulletStrength)
        arcade.Sound(parameters.SOUND_SHOOT).play()
        return bullet
    

    def kill(self):
        drop = Drop("sprites/drops/17.png", 1)
        drop.setup(2, self.center_x, self.center_y)
        self.remove_from_sprite_lists()
        return drop
    
    def hit(self, damage):
        shieldDmg = min(self.shieldCurrent, damage)
        hullDmg = damage - shieldDmg
        self.shieldCurrent -= shieldDmg
        self.health -= hullDmg