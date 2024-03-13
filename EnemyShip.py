from NPO import NonPlayerObject
from Bullet import Bullet
import math
import parameters

class EnemyShip(NonPlayerObject):
    def setup(self,center_x, center_y, velocity, angle):
        self.bulletSpeed = 10
        self.fireRate = 50
        self.cooldown = self.fireRate
        self.center_x = center_x
        self.center_y = center_y
        self.velocity = velocity
        self.angle = angle 
        self.maxTurn = 3
        self.turnChange = 0
        self.topSpeed = 4
        self.acceleration = 2
        self.bulletStrength = 1

    def track(self, player_x, player_y):
        deltaX = player_x - self.center_x
        deltaY = player_y - self.center_y
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

    def update(self):
        self.angle += self.turnChange
        angleRad = math.radians(self.angle)
        deltaX, deltaY = self.velocity
        deltaX += -self.acceleration * math.sin(angleRad)
        deltaY += self.acceleration * math.cos(angleRad)
        speed = math.sqrt(deltaX*deltaX + deltaY*deltaY)
        if speed > self.topSpeed:
            deltaX *= self.topSpeed/speed
            deltaY *= self.topSpeed/speed
        self.velocity = (deltaX, deltaY)
        if self.cooldown > 0:
            self.cooldown -= 1
        super().update()

    def fire(self):
        self.cooldown = self.fireRate
        bullet = Bullet("sprites/asset/laser.png", parameters.SCALING)
        angleRad = math.radians(self.angle)
        x = -self.bulletSpeed * math.sin(angleRad)
        y = self.bulletSpeed * math.cos(angleRad)
        bullet.setup((x,y), self.center_x, self.center_y, self.angle, self.bulletStrength)
        return bullet