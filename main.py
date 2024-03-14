
import arcade
import random
# from NPO import NonPlayerObject
from Asteroid import Asteroid
from EnemyShip import EnemyShip
from PlayerShip import PlayerShip
import parameters



# arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREN_TITLE)
# arcade.set_background_color(arcade.color.BLACK)
# arcade.start_render()


# arcade.finish_render()

# arcade.run()

class Game(arcade.Window):
    def __init__(self):
        super().__init__(parameters.SCREEN_WIDTH, parameters.SCREEN_HEIGHT, parameters.SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.setup()

    def setup(self):
        self.enemies_list = arcade.SpriteList()
        self.asteroids_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.player_bullet_list = arcade.SpriteList()
        self.enemy_bullets_list = arcade.SpriteList()
        self.drop_list = arcade.SpriteList()
        self.paused = False
        self.player = PlayerShip("sprites/PlayerShip/tile000.png", parameters.SCALING)
        self.enemy_textures = arcade.texture.load_spritesheet("sprites\EnemiesShips\EnemiesSpriteSheet.png", 32, 32, 6, 90)
        self.player.setUp()
        self.player.center_y = self.height / 2
        self.player.center_x = self.width / 2
        self.all_sprites.append(self.player)
        arcade.schedule(self.add_asteroid, 2.0)
        arcade.schedule(self.add_enemy, 10)
        self.score = 0
        self.firing = False


    def on_draw(self):
        arcade.start_render()
        self.all_sprites.draw()
        arcade.draw_text(self.score, 10, 10, arcade.color.YELLOW, 20)

    def add_enemy(self, delta_time: float):
        enemy = EnemyShip("sprites/EnemiesShips/tile000.png", parameters.SCALING*2)
        side = random.randint(0,3)
        center_x = 0
        center_y = 0
        velocity = 0 
        angle = 0
        if (side == 0):
            # comming in from top
            center_x = random.randint(10, parameters.SCREEN_WIDTH - 10)
            center_y = parameters.SCREEN_HEIGHT + random.randint(10,80)
            velocity = (0,-4)
            angle = 180
        elif (side == 1):
            # comming in from right
            center_x = parameters.SCREEN_WIDTH + random.randint(10,80)
            center_y = random.randint(10, parameters.SCREEN_HEIGHT - 10)
            velocity = (-4,0)
            angle = 270
        elif (side == 2):
            # comming in from bottom
            center_y = 0 - random.randint(10,80)
            center_x = random.randint(10, parameters.SCREEN_WIDTH - 10)
            velocity = (0,4)
            angle = 0
        elif (side == 3):
            # comming in from left
            center_x = 0 - random.randint(10,80)
            center_y = random.randint(10, parameters.SCREEN_HEIGHT - 10)
            velocity = (4,0)   
            angle = 90 
        enemy.setup(center_x, center_y, velocity, angle)
        type = random.randint(1,3)
        start = 0
        end = 0
        if type == 1:
            start = 18
            end = 30
        elif type == 2:
            start = 36
            end = 48
        elif type == 3:
            start = 66
            end = 78
        textures = self.enemy_textures[start:end]
        textures.reverse()
        enemy.set_textures(textures)
        self.enemies_list.append(enemy)
        self.all_sprites.append(enemy) 

    def add_asteroid(self, delta_time: float):
        if len(self.asteroids_list) >= 5:
            return
        asteroid = Asteroid("sprites/asset/meteor.png", parameters.SCALING*random.randint(1,6)/2)
        asteroid.setRotation()
        side = random.randint(0,3)
        if (side == 0):
            # comming in from top
            asteroid.center_x = random.randint(10, parameters.SCREEN_WIDTH - 10)
            asteroid.center_y = parameters.SCREEN_HEIGHT + random.randint(10,80)
            asteroid.velocity = (random.randint(-2, 2), random.randint(-6,-2))
        elif (side == 1):
            # comming in from right
            asteroid.center_x = parameters.SCREEN_WIDTH + random.randint(10,80)
            asteroid.center_y = random.randint(10, parameters.SCREEN_HEIGHT - 10)
            asteroid.velocity = (random.randint(-6,-2), random.randint(-2,2))
        elif (side == 2):
            # comming in from bottom
            asteroid.center_x = random.randint(10, parameters.SCREEN_WIDTH - 10)
            asteroid.center_y = 0 - random.randint(10,80)
            asteroid.velocity = (random.randint(-2, 2), random.randint(2,6))
        elif (side == 3):
            # comming in from left
            asteroid.center_x = 0 - random.randint(10,80)
            asteroid.center_y = random.randint(10, parameters.SCREEN_HEIGHT - 10)
            asteroid.velocity = (random.randint(2,6), random.randint(-2,2))
        self.asteroids_list.append(asteroid)
        self.all_sprites.append(asteroid)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q:
            arcade.close_window()

        if symbol == arcade.key.P:
            self.paused = not self.paused

        if symbol == arcade.key.W or symbol == arcade.key.UP:
            self.player.accelerating = 1
        
        if symbol == arcade.key.A or symbol == arcade.key.LEFT:
            self.player.turnDir = 1
            self.player.change_animation(1)

        if symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            self.player.turnDir = -1
            self.player.change_animation(2)

        if symbol == arcade.key.SPACE:
            self.firing = True
        if symbol == arcade.key.R:
            self.setup()
            
    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.W or symbol == arcade.key.UP:
            self.player.accelerating = 0
        
        if symbol == arcade.key.A or symbol == arcade.key.LEFT or symbol == arcade.key.S or symbol == arcade.key.RIGHT:
            self.player.turnDir = 0
            self.player.change_animation(0)

        if symbol == arcade.key.SPACE:
            self.firing = False

    def on_update(self, delta_time: float):
        # return super().on_update(delta_time)
        # self.all_sprites.add_spatial_hashes()
        if self.paused:
            return
        if self.firing:
            if (self.player.cooldown == 0):
                bullet = self.player.fire()
                self.player_bullet_list.append(bullet)
                self.all_sprites.append(bullet)
        for enemy in self.enemies_list:
            enemy.track(self.player.center_x, self.player.center_y)
            if (enemy.cooldown == 0):
                bullet = enemy.fire()
                self.enemy_bullets_list.append(bullet)
                self.all_sprites.append(bullet)

        self.all_sprites.update()
        for drop in self.drop_list:
            if drop.collides_with_sprite(self.player):
                drop.remove_from_sprite_lists()
                self.score += 1
                arcade.Sound(parameters.SOUND_PICKUP).play()
        if self.player.collides_with_list(self.asteroids_list) or self.player.collides_with_list(self.enemies_list) or self.player.collides_with_list(self.enemy_bullets_list):
            self.player.remove_from_sprite_lists()
        for bullet in self.player_bullet_list:
            hitList = bullet.collides_with_list(self.asteroids_list)
            if len(hitList) > 0:
                bullet.remove_from_sprite_lists()
                arcade.Sound(parameters.SOUND_SHIP_DIE).play()
                for object in hitList:
                    drop = object.kill()
                    if (drop):
                        self.drop_list.append(drop)
                        self.all_sprites.append(drop)
            hitList = bullet.collides_with_list(self.enemies_list)
            if len(hitList) > 0:
                bullet.remove_from_sprite_lists()
                arcade.Sound(parameters.SOUND_ASTEROID_DIE).play()
                for object in hitList:
                    drop = object.kill()
                    if (drop):
                        self.drop_list.append(drop)
                        self.all_sprites.append(drop)

if __name__ == "__main__":
    app = Game()
    
    arcade.run()