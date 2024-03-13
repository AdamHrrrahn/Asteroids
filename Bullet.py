from NPO import NonPlayerObject

class Bullet(NonPlayerObject):
    def setup(self, velocity, x, y, angle, strength):
        self.velocity = velocity
        self.angle = angle
        self.center_x = x
        self.center_y = y
        self.strength = strength