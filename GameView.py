import arcade
import random
# from NPO import NonPlayerObject
from Asteroid import Asteroid
from EnemyShip import EnemyShip
from PlayerShip import PlayerShip
from Bullet import Bullet
from Drop import Drop
from Station import Station
import parameters
import math

class GameView(arcade.View):
    def __init__(self, player):
        super().__init__()
        arcade.set_background_color(arcade.color.BLACK)
        self.player = player
        self.setup()

    def setViews(self, pause, station):
        self.pauseView = pause
        self.stationView = station

    def setup(self):
        self.enemies_list = arcade.SpriteList()
        self.asteroids_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.player_bullet_list = arcade.SpriteList()
        self.enemy_bullets_list = arcade.SpriteList()
        self.drop_list = arcade.SpriteList()
        self.paused = False
        self.station = Station("sprites\station\B12.png", parameters.SCALING/2)
        self.station.center_y = parameters.SCREEN_HEIGHT / 2
        self.station.center_x = parameters.SCREEN_WIDTH / 2
        self.all_sprites.append(self.station)
        self.enemy_textures = arcade.texture.load_spritesheet("sprites\EnemiesShips\EnemiesSpriteSheet.png", 32, 32, 6, 90)
        self.player.setUp()
        self.player.center_y = parameters.SCREEN_HEIGHT / 2
        self.player.center_x = parameters.SCREEN_WIDTH / 2
        self.all_sprites.append(self.player)
        # arcade.schedule(self.add_asteroid, 2.0)
        # arcade.schedule(self.add_enemy, 10)
        self.asteroidCooldown = parameters.ASTEROID_SPAWN_RATE
        self.enemyCooldown = parameters.ENEMY_SPAWN_RATE
        self.firing = False
        self.dead = False
        self.canDock = True


    def on_draw(self):
        arcade.start_render()
        self.station.draw()
        # self.all_sprites.draw()
        self.asteroids_list.draw()
        # self.enemies_list.draw()
        self.drop_list.draw()
        for enemy in self.enemies_list:
            enemy.draw()
            if enemy.shieldCurrent > 0:
                arcade.draw_circle_outline(enemy.center_x, enemy.center_y, 20*parameters.SCALING, arcade.color.BLUE, 2)
        self.player_bullet_list.draw()
        self.enemy_bullets_list.draw()
        if self.player.shieldCurrent > 0:
            arcade.draw_circle_outline(self.player.center_x, self.player.center_y, 20*parameters.SCALING, arcade.color.BLUE, 2)
        self.player.draw()
        # arcade.draw_text(self.player.wallet, 10, 10, arcade.color.YELLOW, 20)
        arcade.draw_text(f"Health:  {self.player.health}", 10, parameters.SCREEN_HEIGHT-30, arcade.color.RED, 20)
        arcade.draw_text(f"Shields: {self.player.shieldCurrent}", 10, parameters.SCREEN_HEIGHT - 60, arcade.color.BLUE, 20)
        arcade.draw_text(f"Carco: {self.player.cargo}/{self.player.maxCargo}", 10, parameters.SCREEN_HEIGHT - 90, arcade.color.YELLOW, 20)
        if self.canDock:
            arcade.draw_text("Press 'L' to dock", parameters.SCREEN_WIDTH/2, 10, arcade.color.WHITE, 20)

    def add_enemy(self):
        enemy = EnemyShip("sprites/EnemiesShips/tile000.png", parameters.SCALING*2)
        side = random.randint(0,3)
        center_x = 0
        center_y = 0
        velocity = 0 
        angle = 0
        if (side == 0):
            # comming in from top
            center_x = random.randint(10, parameters.SCREEN_WIDTH - 10)
            center_y = parameters.SCREEN_HEIGHT + random.randint(10,60)
            velocity = (0,-4)
            angle = 180
        elif (side == 1):
            # comming in from right
            center_x = parameters.SCREEN_WIDTH + random.randint(10,60)
            center_y = random.randint(10, parameters.SCREEN_HEIGHT - 10)
            velocity = (-4,0)
            angle = 270
        elif (side == 2):
            # comming in from bottom
            center_y = 0 - random.randint(10,60)
            center_x = random.randint(10, parameters.SCREEN_WIDTH - 10)
            velocity = (0,4)
            angle = 0
        elif (side == 3):
            # comming in from left
            center_x = 0 - random.randint(10,60)
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

    def add_asteroid(self):
        if len(self.asteroids_list) >= 5:
            return
        num = random.uniform(1,5)
        asteroid = Asteroid("sprites/asset/meteor.png", parameters.SCALING*num/2)
        asteroid.setRotation()
        asteroid.setSize(math.ceil(num))
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
        # if symbol == arcade.key.Q:
        #     arcade.close_window()

        if symbol == arcade.key.P:
            # self.paused = not self.paused
            self.window.show_view(self.pauseView)

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
        # if symbol == arcade.key.R:
        #     self.setup()
        if self.canDock and symbol == arcade.key.L:
            arcade.Sound(parameters.SOUND_LANDING).play()
            self.window.show_view(self.stationView)
            
    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.W or symbol == arcade.key.UP:
            self.player.accelerating = 0
        
        if symbol == arcade.key.A or symbol == arcade.key.LEFT or symbol == arcade.key.S or symbol == arcade.key.RIGHT:
            self.player.turnDir = 0
            self.player.change_animation(0)

        if symbol == arcade.key.SPACE:
            self.firing = False

    def asteroid_kill(self, object):
        arcade.Sound(parameters.SOUND_ASTEROID_DIE).play()
        drops, children = object.kill()
        self.drop_list.extend(drops)
        self.all_sprites.extend(drops)
        if (len(children) > 0):
            self.asteroids_list.extend(children)
            self.all_sprites.extend(children)

    def ship_kill(self, object):
        arcade.Sound(parameters.SOUND_SHIP_DIE).play()
        drop = object.kill()
        self.drop_list.append(drop)
        self.all_sprites.append(drop)

    def bullet_kill(self, bullet):
        bullet.remove_from_sprite_lists()

    def on_update(self, delta_time: float):
        self.asteroidCooldown -= 1
        self.enemyCooldown -= 1
        if self.asteroidCooldown == 0:
            self.asteroidCooldown = parameters.ASTEROID_SPAWN_RATE
            self.add_asteroid()
        if self.enemyCooldown == 0:
            self.enemyCooldown = parameters.ENEMY_SPAWN_RATE
            self.add_enemy()
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
                if self.player.cargo < self.player.maxCargo:
                    drop.remove_from_sprite_lists()
                    self.player.cargoValue += drop.value
                    self.player.cargo += 1
                    arcade.Sound(parameters.SOUND_PICKUP).play()
        collision_list = self.player.collides_with_list(self.asteroids_list)
        collision_list.extend(self.player.collides_with_list(self.enemies_list))
        collision_list.extend(self.player.collides_with_list(self.enemy_bullets_list))
        for object in collision_list:
            damage = min(self.player.health+self.player.shieldCurrent, object.health+object.shieldCurrent)
            self.player.hit(damage)
            object.hit(damage)
            if self.player.health <= 0:
                self.player.remove_from_sprite_lists()
                arcade.Sound(parameters.SOUND_SHIP_DIE).play()
                self.player.center_x = -parameters.MAP_WIDTH*3
                self.player.center_y = -parameters.MAP_HEIGHT*3
            if object.health <= 0:
                if object is EnemyShip:
                    self.ship_kill(object)
                elif object is Asteroid:
                    self.asteroid_kill(object)
                elif object is Bullet:
                    self.bullet_kill(object)
                    arcade.Sound(parameters.SOUND_SHIP_HIT).play()
        for bullet in self.player_bullet_list:
            hitList = bullet.collides_with_list(self.asteroids_list)
            if len(hitList) > 0:
                self.bullet_kill(bullet)
                for object in hitList:
                    object.health -= bullet.strength
                    if object.health <= 0:
                        self.asteroid_kill(object)
                    else:
                        arcade.Sound(parameters.SOUND_ASTEROID_HIT).play()
            hitList = bullet.collides_with_list(self.enemies_list)
            if len(hitList) > 0:
                self.bullet_kill(bullet)
                for object in hitList:
                    object.hit(bullet.strength)
                    if object.health <= 0:
                        self.ship_kill(object)
                    else:
                        arcade.Sound(parameters.SOUND_SHIP_HIT).play()
        if (math.hypot(self.player.center_x-parameters.SCREEN_WIDTH/2, self.player.center_y-parameters.SCREEN_HEIGHT/2) < 100):
            self.canDock = True
        else:
            self.canDock = False