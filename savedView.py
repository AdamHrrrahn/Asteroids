import arcade
import parameters

class SavedView(arcade.View):
    def __init__(self, view):
        super().__init__()
        self.nextView = view

    def on_draw(self):
        self.clear()
        arcade.draw_text("Game Saved", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2, arcade.color.GREEN, 40, anchor_x="center")

    def on_key_press(self, symbol, modifiers):
        self.window.show_view(self.nextView)