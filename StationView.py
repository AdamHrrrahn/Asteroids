import arcade
import parameters

class StationView(arcade.View):
    def setViews(self, game, player, upgrade, saveView):
        self.gameView = game
        self.upgradeView = upgrade
        self.saveView = saveView
        self.selected = 0
        self.ship = arcade.Sprite("sprites/PlayerShip/tile000.png", parameters.SCALING)
        self.ship.center_x = parameters.SCREEN_WIDTH/2
        self.ship.center_y = parameters.SCREEN_HEIGHT*3/4 
        self.player = player

    def on_draw(self):
        self.clear()
        self.ship.draw()
        arcade.draw_text(f"${self.player.wallet}", 10, 10, arcade.color.YELLOW, 20)
        arcade.draw_text("Launch", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2+120, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text(f"Repair: ${self.player.maxHealth*(self.player.maxHealth - self.player.health)}", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2+60, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text(f"Sell cargo: ${self.player.cargoValue}", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Upgrade Ship", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2-60, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Save", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2-120, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Load", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2-180, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Quit", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2-240, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_rectangle_outline(parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2+130-60*self.selected, 180, 40, arcade.color.YELLOW)

    def launch_button(self):
        self.selected = 0
        arcade.Sound(parameters.SOUND_TAKEOFF).play()
        self.gameView.resetPosition()
        self.window.show_view(self.gameView)
        
    def repair_button(self):
        repairCost = self.player.maxHealth*(self.player.maxHealth - self.player.health)
        if (self.player.health < self.player.maxHealth) and (self.player.wallet >= repairCost):
            self.player.wallet -= repairCost
            self.player.health = self.player.maxHealth
            arcade.Sound(parameters.SOUND_REPAIR).play()

    def sell_cargo_button(self):
        if self.player.cargo > 0:
            self.player.wallet += self.player.cargoValue
            self.player.cargo = 0
            self.player.cargoValue = 0
            arcade.Sound(parameters.SOUND_SELL_CARGO).play()

    def upgrade_button(self):
        self.selected = 0
        self.window.show_view(self.upgradeView)

    def save_button(self):
        self.selected = 0
        self.saveView.setState(1, self)
        self.window.show_view(self.saveView)

    def load_button(self):
        self.selected = 0
        self.saveView.setState(0, self)
        self.window.show_view(self.saveView)

    def quit_button(self):
        arcade.close_window()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.W or symbol == arcade.key.UP:
            if self.selected > 0:
                self.selected -= 1

        if symbol == arcade.key.S or symbol == arcade.key.DOWN:
            if self.selected < 6:
                self.selected += 1

        if symbol == arcade.key.SPACE:
            if self.selected == 0:
                self.launch_button()
            elif self.selected == 1:
                self.repair_button()
            elif self.selected == 2:
                self.sell_cargo_button()
            elif self.selected == 3:
                self.upgrade_button()
            elif self.selected == 4:
                self.save_button()
            elif self.selected == 5:
                self.load_button()
            elif self.selected == 6:
                self.quit_button() 
