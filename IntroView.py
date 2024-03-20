import arcade
import parameters

class IntroView(arcade.View):
    def setViews(self, game):
        arcade.set_background_color(arcade.color.BLACK)
        self.gameView = game

    def on_draw(self):
        arcade.draw_text("Welcome To Asteroids", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT-100, arcade.color.YELLOW, 40, anchor_x="center")
        arcade.draw_text("To turn ship usef left and right or a and d", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT-220, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Move your ship Forward using w or up", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT-280, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Hold space to fire your ship's gun", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT-340, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Destroy asteroids and enemies and gather their drops", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT-400, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Return to the station to sell your loot and upgrade your ship", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT-460, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Press p to pause and use space to select menu options", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT-520, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Press any key to start", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2-580, arcade.color.WHITE, 20, anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):
        arcade.Sound(parameters.SOUND_START_GAME).play()
        self.window.show_view(self.gameView)