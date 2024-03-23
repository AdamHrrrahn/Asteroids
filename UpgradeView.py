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
        self.upgrade = [self.upgrade_max_health, self.upgrade_max_shields, self.upgrade_shield_regen, self.upgrade_max_cargo, self.upgrade_fire_rate, self.upgrade_bullet_damage, self.upgrade_acceleration, self.upgrade_top_speed, self.upgrade_turn_speed]

    def on_draw(self):
        self.clear()
        self.ship1.draw()
        self.ship2.draw()
        arcade.draw_text(f"${self.player.wallet}", 10, 10, arcade.color.YELLOW, 20)
        arcade.draw_text(f"Upgrade cost: ${self.player.upgradeCost}", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2+300, arcade.color.WHITE, 20, anchor_x="center")

        arcade.draw_text(f"Max Health: {self.player.maxHealth}" + ("Maxed" if self.player.maxed[0] else f"->{self.player.maxHealth+1}"), parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2+240, arcade.color.GRAY if self.player.maxed[0] else arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text(f"Max Shields: {self.player.shieldMax}" + ("Maxed" if self.player.maxed[1] else f"->{self.player.shieldMax+1}"), parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2+180, arcade.color.GRAY if self.player.maxed[1] else arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text(f"Shield regen: {self.player.shieldRegen}" + ("Maxed" if self.player.maxed[2] else f"->{self.player.shieldRegen+1}"), parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2+120, arcade.color.GRAY if self.player.maxed[2] else arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text(f"Cargo Space: {self.player.maxCargo}" + ("Maxed" if self.player.maxed[3] else f"->{self.player.maxCargo+1}"), parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2+60, arcade.color.GRAY if self.player.maxed[3] else arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text(f"Fire rate: {self.player.maxHealth}" + ("Maxed" if self.player.maxed[4] else f"->{self.player.maxHealth+1}"), parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2, arcade.color.GRAY if self.player.maxed[4] else arcade.color.WHITE, 20, anchor_x="center")

        arcade.draw_text(f"Bullet Damage: {self.player.bulletStrength}" + ("Maxed" if self.player.maxed[5] else f"->{self.player.bulletStrength+1}"), parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2-60, arcade.color.GRAY if self.player.maxed[5] else arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text(f"Acceleration: {self.player.acceleration}" + ("Maxed" if self.player.maxed[6] else f"->{self.player.acceleration+0.5}"), parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2-120, arcade.color.GRAY if self.player.maxed[7] else arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text(f"Top Speed: {self.player.topSpeed}" + ("Maxed" if self.player.maxed[7] else f"->{self.player.topSpeed+0.5}"), parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2-180, arcade.color.GRAY if self.player.maxed[8] else arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text(f"Turn Speed: {self.player.turnSpeed}" + ("Maxed" if self.player.maxed[8] else f"->{self.player.turnSpeed+0.5}"), parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2-240, arcade.color.GRAY if self.player.maxed[9] else arcade.color.WHITE, 20, anchor_x="center")

        arcade.draw_text("Return", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2-300, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_rectangle_outline(parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2+250-60*self.selected, 220, 40, arcade.color.YELLOW)

    def return_button(self):
        self.selected = 0
        self.window.show_view(self.stationView)

    def upgrade_max_health(self):
        self.player.maxHealth += 1
        if self.player.maxHealth == 10:
            self.player.maxed[0] = True

    def upgrade_max_shields(self):
        self.player.shieldMax += 1
        if self.player.shieldMax == 10:
            self.player.maxed[1] = True

    def upgrade_shield_regen(self):
        self.player.shieldRegen += 1
        if self.player.shieldRegen == 5:
            self.player.maxed[2] = True

    def upgrade_max_cargo(self):
        self.player.maxCargo += 1
        if self.player.maxCargo == 20:
            self.player.maxed[3] = True

    def upgrade_fire_rate(self):
        self.player.fireRate -= 5
        if self.player.fireRate == 5:
            self.player.maxed[4] = True

    def upgrade_bullet_damage(self):
        self.player.bulletStrength += 1
        if self.player.bulletStrength == 5:
            self.player.maxed[5] = True

    def upgrade_acceleration(self):
        self.player.acceleration += 0.5
        if self.player.acceleration == 3:
            self.player.maxed[6] = True

    def upgrade_top_speed(self):
        self.player.topSpeed += 0.5
        if self.player.topSpeed == 8:
            self.player.maxed[7] = True

    def upgrade_turn_speed(self):
        self.player.turnSpeed += 0.5
        if self.player.turnSpeed == 6:
            self.player.maxed[8] = True

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
            elif not (self.player.maxed[self.selected]):
                if self.player.wallet >= self.player.upgradeCost:
                    self.upgrade[self.selected]()
                    self.player.wallet -= self.player.upgradeCost
                    self.player.upgradeCost = math.ceil(self.player.upgradeCost * 1.2)
                    self.player.level += 1
                    arcade.Sound(parameters.SOUND_UPGRADE).play()
