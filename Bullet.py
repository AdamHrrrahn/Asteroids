from NPO import NonPlayerObject

class Bullet(NonPlayerObject):
    def setup(self, velocity, x, y, angle, strength):
        self.velocity = velocity
        self.angle = angle
        self.center_x = x
        self.center_y = y
        self.strength = strength
        self.health = strength
        self.shieldCurrent = 0

    def hit(self, damage):
        self.remove_from_sprite_lists()