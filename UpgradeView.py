import arcade
import parameters
import math

class UpgradeView(arcade.View):
    def setViews(self, station, player):
        self.stationView = station
        self.selected = 0
        self.ship1 = arcade.Sprite("sprites/PlayerShip/tile000.png", parameters.SCALING)
        self.ship1.center_x = parameters.SCREEN_WIDTH*3/4
        self.ship1.center_y = parameters.SCREEN_HEIGHT/2
        self.ship2 = arcade.Sprite("sprites/PlayerShip/tile000.png", parameters.SCALING)
        self.ship2.center_x = parameters.SCREEN_WIDTH*1/4
        self.ship2.center_y = parameters.SCREEN_HEIGHT/2
        self.player = player
        self.upgradeCost = 5
        self.maxed = [False, False, False, False, False, False, False, False, False, False]
        self.upgrade = [self.upgrade_max_health, self.upgrade_max_shields, self.upgrade_shield_regen, self.upgrade_max_cargo, self.upgrade_fire_rate, self.upgrade_bullet_damage, self.upgrade_acceleration, self.upgrade_top_speed, self.upgrade_turn_speed]

    def on_draw(self):
        self.clear()
        self.ship1.draw()
        self.ship2.draw()
        arcade.draw_text(f"${self.player.wallet}", 10, 10, arcade.color.YELLOW, 20)
        arcade.draw_text(f"Upgrade cost: ${self.upgradeCost}", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2+300, arcade.color.WHITE, 20, anchor_x="center")

        arcade.draw_text("Max Health", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2+240, arcade.color.GRAY if self.maxed[0] else arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Max Shields", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2+180, arcade.color.GRAY if self.maxed[1] else arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Shield regen", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2+120, arcade.color.GRAY if self.maxed[2] else arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Cargo Space", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2+60, arcade.color.GRAY if self.maxed[3] else arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Fire rate", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2, arcade.color.GRAY if self.maxed[4] else arcade.color.WHITE, 20, anchor_x="center")

        arcade.draw_text("Bullet Damage", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2-60, arcade.color.GRAY if self.maxed[5] else arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Acceleration", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2-120, arcade.color.GRAY if self.maxed[7] else arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Top Speed", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2-180, arcade.color.GRAY if self.maxed[8] else arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Turn Speed", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2-240, arcade.color.GRAY if self.maxed[9] else arcade.color.WHITE, 20, anchor_x="center")

        arcade.draw_text("Return", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2-300, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_rectangle_outline(parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2+250-60*self.selected, 220, 40, arcade.color.YELLOW)

    def return_button(self):
        self.selected = 0
        self.window.show_view(self.stationView)

    def upgrade_max_health(self):
        self.player.maxHealth += 1
        if self.player.maxHealth == 10:
            self.maxed[0] = True

    def upgrade_max_shields(self):
        self.player.maxShields += 1
        if self.player.maxShields == 10:
            self.maxed[1] = True

    def upgrade_shield_regen(self):
        self.player.ShieldRegen += 1
        if self.player.ShieldRegen == 5:
            self.maxed[2] = True

    def upgrade_max_cargo(self):
        self.player.maxCargo += 1
        if self.player.maxHealth == 20:
            self.maxed[3] = True

    def upgrade_fire_rate(self):
        self.player.fireRate -= 5
        if self.player.fireRate == 5:
            self.maxed[4] = True

    def upgrade_bullet_damage(self):
        self.player.bulletStrength += 1
        if self.player.bulletStrength == 5:
            self.maxed[5] = True

    def upgrade_acceleration(self):
        self.player.acceleration += 1
        if self.player.acceleration == 3:
            self.maxed[6] = True

    def upgrade_top_speed(self):
        self.player.topSpeed += 1
        if self.player.topSpeed == 10:
            self.maxed[7] = True

    def upgrade_turn_speed(self):
        self.player.turnSpeed += 1
        if self.player.turnSpeed == 10:
            self.maxed[8] = True

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.W or symbol == arcade.key.UP:
            if self.selected > 0:
                self.selected -= 1

        if symbol == arcade.key.S or symbol == arcade.key.DOWN:
            if self.selected < 9:
                self.selected += 1

        if symbol == arcade.key.SPACE:
            if self.selected == 9:
                self.return_button()
            elif not (self.maxed[self.selected]):
                if self.player.wallet >= self.upgradeCost:
                    self.upgrade[self.selected]()
                    self.player.wallet -= self.upgradeCost
                    self.upgradeCost = math.ceil(self.upgradeCost * 1.2)
                    arcade.Sound(parameters.SOUND_UPGRADE).play()
