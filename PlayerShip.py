import arcade
# from Object import Object
import math
import parameters
import pickle
from Bullet import Bullet

class PlayerShip(arcade.Sprite):
    def setUp(self):
        self.angle = 0
        self.velocity = (0,0)
        self.turnSpeed = 3.5
        self.acceleration = 0.5
        self.accelerating = 0
        self.turnDir = 0
        self.bulletSpeed = 10
        self.bulletStrength = 1
        self.fireRate = 30
        self.cooldown = 0
        self.topSpeed = 3.5
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
        self.wallet = 0
        self.cargo = 0
        self.maxCargo = 3
        self.cargoValue = 0
        self.maxed = [False, False, False, False, False, False, False, False, False, False]
        self.upgradeCost = 5
        self.level = 1



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

    def save(self, file):
        db = {"MaxHealth" : self.maxHealth, 
              "currentHealth":self.health, 
              "maxShields":self.shieldMax, 
              "currentShields":self.shieldCurrent, 
              "shieldRegen":self.shieldRegen,
              "turnSpeed": self.turnSpeed,
              "acceleration":self.acceleration,
              "bulletSpeed":self.bulletSpeed,
              "bulletStrength":self.bulletStrength,
              "fireRate":self.fireRate,
              "topSpeed":self.topSpeed,
              "wallet":self.wallet,
              "cargo":self.cargo,
              "maxCargo":self.maxCargo,
              "cargoValue":self.cargoValue,
              "maxed":self.maxed,
              "upgradeCost":self.upgradeCost,
              "level":self.level}
        dbfile = open(f"savefile{file}", 'wb')
        pickle.dump(db, dbfile)
        dbfile.close()

    def load(self, file):
        dbfile = open(f"savefile{file}", 'rb')
        data = pickle.load(dbfile)
        self.maxHealth = int(data["MaxHealth"])
        self.health = int(data["currentHealth"])
        self.shieldMax = int(data["maxShields"])
        self.shieldCurrent = int(data["currentShields"])
        self.shieldRegen = int(data["shieldRegen"])
        self.turnSpeed = float(data["turnSpeed"])
        self.acceleration = float(data["acceleration"])
        self.bulletSpeed = int(data["bulletSpeed"])
        self.bulletStrength = int(data["bulletStrength"])
        self.fireRate = int(data["fireRate"])
        self.topSpeed = int(data["topSpeed"])
        self.wallet = int(data["wallet"])
        self.cargo = int(data["cargo"])
        self.maxCargo = int(data["maxCargo"])
        self.cargoValue = int(data["cargoValue"])
        self.maxed = data["maxed"]
        self.upgradeCost = int(data["upgradeCost"])
        self.level = int(data["level"])
        dbfile.close()
