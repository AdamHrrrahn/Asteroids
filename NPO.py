# from Object import Object
import arcade
import parameters


class NonPlayerObject(arcade.Sprite):
    def update(self):
        super().update()
        if ((self.center_x < -100) or (self.center_x > parameters.SCREEN_WIDTH + 100) or (self.center_y < -100) or (self.center_y > parameters.SCREEN_HEIGHT + 100)):
            self.remove_from_sprite_lists()

    
    def kill(self):
        drop = arcade.Sprite("sprites/asset/flare.png", 1)
        drop.top = self.top 
        drop.left = self.left
        self.remove_from_sprite_lists()
        return drop
