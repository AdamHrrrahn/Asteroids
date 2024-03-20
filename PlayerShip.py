import arcade
# from Object import Object
import math
import parameters
from Bullet import Bullet

class PlayerShip(arcade.Sprite):
    def setUp(self):
        self.angle = 0
        self.velocity = (0,0)
        self.turnSpeed = 3
        self.acceleration = 0.5
        self.accelerating = 0
        self.turnDir = 0
        self.bulletSpeed = 10
        self.bulletStrength = 1
        self.bulletCount = 1
        self.fireRate = 30
        self.cooldown = 0
        self.topSpeed = 3
        self.anamationSpeed = 10
        self.animationFrame = 0
        self.curTexture = 0
        self.straight_textures = []
        self.turn_left_textures = []
        self.turn_right_textures = []
        self.get_textures()
        self.current_texture_list = self.straight_textures
        self.health = 3
        self.maxHealth = 3
        self.shieldMax = 2
        self.shieldCurrent = 2
        self.shieldCooldown = 300
        self.shieldRegen = 1
        self.wallet = 11
        self.cargo = 0
        self.maxCargo = 3
        self.cargoValue = 0
        self.maxed = [False, False, False, False, False, False, False, False, False, False]
        self.upgradeCost = 5



    def get_textures(self):
        textures = arcade.texture.load_spritesheet("sprites\PlayerShip\PlayerShipSpriteSheet.png.png", 32, 32, 4, 12)
        for i in range(0,4):
            self.straight_textures.append(textures[i])
        for i in range(4,7):
            self.turn_right_textures.append(textures[i])
        for i in range(8,11):
            self.turn_left_textures.append(textures[i])


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
                self.shieldCooldown = 300
                self.shieldCurrent += self.shieldRegen
                if self.shieldCurrent > self.shieldMax:
                    self.shieldCurrent = self.shieldMax

        self.animationFrame += 1
        if (self.animationFrame == self.anamationSpeed):
            self.animationFrame = 0
            self.curTexture = (self.curTexture + 1) % len(self.current_texture_list)
            self.texture = self.current_texture_list[self.curTexture]

        self.angle += self.turnSpeed * self.turnDir
        angleRad = math.radians(self.angle)
        deltaX, deltaY = self.velocity
        deltaX += -self.acceleration * self.accelerating * math.sin(angleRad)
        deltaY += self.acceleration * self.accelerating * math.cos(angleRad)
        speed = math.sqrt(deltaX*deltaX + deltaY*deltaY)
        if speed > self.topSpeed:
            deltaX *= self.topSpeed/speed
            deltaY *= self.topSpeed/speed
        self.velocity = (deltaX, deltaY)
        if (self.cooldown > 0):
            self.cooldown -= 1
        super().update()
        if self.center_y > parameters.SCREEN_HEIGHT:
            self.center_y -= parameters.SCREEN_HEIGHT
        if self.center_y < 0:
            self.center_y += parameters.SCREEN_HEIGHT
        if self.center_x < 0:
            self.center_x += parameters.SCREEN_WIDTH
        if self.center_x > parameters.SCREEN_WIDTH:
            self.center_x -= parameters.SCREEN_WIDTH

    def fire(self):
        self.cooldown = self.fireRate
        bullet = Bullet("sprites/asset/laser.png", parameters.SCALING)
        angleRad = math.radians(self.angle)
        x = -self.bulletSpeed * math.sin(angleRad)
        y = self.bulletSpeed * math.cos(angleRad)
        bullet.setup((x,y), self.center_x, self.center_y, self.angle, self.bulletStrength)
        arcade.Sound(parameters.SOUND_SHOOT).play()
        return bullet
    
    def hit(self, damage):
        shieldDmg = min(self.shieldCurrent, damage)
        hullDmg = damage - shieldDmg
        self.shieldCurrent -= shieldDmg
        self.health -= hullDmg
