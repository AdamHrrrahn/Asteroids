import arcade
import parameters

class IntroView(arcade.View):
    def setViews(self, game, saveView, player):
        arcade.set_background_color(arcade.color.BLACK)
        self.gameView = game
        self.player = player
        self.saveView = saveView
        self.selected = 0

    def on_show_view(self):
        self.gameView.setup()

    def on_draw(self):
        self.clear()
        arcade.draw_text("Welcome To Asteroids", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT-100, arcade.color.YELLOW, 40, anchor_x="center")
        arcade.draw_text("To turn ship usef left and right or a and d", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT-220, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Move your ship Forward using w or up", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT-280, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Hold space to fire your ship's gun", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT-340, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Destroy asteroids and enemies and gather their drops", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT-400, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Return to the station to sell your loot and upgrade your ship", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT-460, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Press p to pause and use space to select menu options", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT-520, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("New Game", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT-580, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Load Game", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT-640, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Quit", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT-700, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_rectangle_outline(parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT-570-60*self.selected, 160, 40, arcade.color.YELLOW)
        # arcade.draw_text("Press any key to start", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2-580, arcade.color.WHITE, 20, anchor_x="center")


    def new_button(self):
        self.selected = 0
        self.player.setUp()
        arcade.Sound(parameters.SOUND_START_GAME).play()
        self.window.show_view(self.gameView)
        
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
            if self.selected < 2:
                self.selected += 1

        if symbol == arcade.key.SPACE:
            if self.selected == 0:
                self.new_button()
            elif self.selected == 1:
                self.load_button()
            elif self.selected == 2:
                self.quit_button()

           