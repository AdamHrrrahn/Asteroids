import arcade
import parameters

class PauseView(arcade.View):
    def setViews(self, game):
        self.gameView = game
        self.selected = 0
        self.player = arcade.Sprite("sprites/PlayerShip/tile000.png", parameters.SCALING)
        self.player.center_x = parameters.SCREEN_WIDTH/2
        self.player.center_y = parameters.SCREEN_HEIGHT*3/4 

    def on_draw(self):
        self.clear()
        self.player.draw()
        arcade.draw_text("Resume", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2+30, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Quit", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2-30, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_rectangle_outline(parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2+40-60*self.selected, 110, 40, arcade.color.YELLOW)

    def resume_button(self):
        self.selected = 0
        self.window.show_view(self.gameView)
        

    def quit_button(self):
        arcade.close_window()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.W or symbol == arcade.key.UP:
            self.selected = 0

        if symbol == arcade.key.S or symbol == arcade.key.DOWN:
            self.selected = 1

        if symbol == arcade.key.SPACE:
            self.quit_button() if self.selected else self.resume_button()