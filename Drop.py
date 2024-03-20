import arcade
import parameters
from NPO import NonPlayerObject

class Drop(NonPlayerObject):
    def setup(self, value, x, y):
        self.value = value
        self.center_x = x
        self.center_y = y