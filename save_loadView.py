import arcade
import parameters
import pickle
from savedView import SavedView

class save_loadView(arcade.View):
    def setViews(self, game, player):
        self.gameView = game
        self.player = player
        self.selected = 0
        self.ship = arcade.Sprite("sprites/PlayerShip/tile000.png", parameters.SCALING)
        self.ship.center_x = parameters.SCREEN_WIDTH/2
        self.ship.center_y = parameters.SCREEN_HEIGHT*3/4 

    def setState(self, state, priorView):
        self.state = state
        self.priorView = priorView
        self.load_saves()

    def on_show_view(self):
        self.load_saves()
    
    def load_saves(self):
        self.saves = []
        for i in range(1,parameters.NUM_SAVE_FILES+1):
            self.saves.append(self.load(i))

    def on_draw(self):
        self.clear()
        self.ship.draw()
        for i in range(0,parameters.NUM_SAVE_FILES):
            arcade.draw_text(self.saves[i][2], parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2+(parameters.NUM_SAVE_FILES-1)*30-i*60, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Cancel", parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2-30-parameters.NUM_SAVE_FILES*30, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_rectangle_outline(parameters.SCREEN_WIDTH/2, parameters.SCREEN_HEIGHT/2+(parameters.NUM_SAVE_FILES-1)*30+10-60*self.selected, 210, 40, arcade.color.YELLOW)

    def save_button(self, file):
        self.selected = 0
        self.player.save(file)
        savedView = SavedView(self.priorView)
        self.window.show_view(savedView)

    def load_button(self, file):
        if int(self.saves[file-1][1]) > 0:
            self.player.load(file)
            arcade.Sound(parameters.SOUND_START_GAME).play()
            self.gameView.setup()
            self.window.show_view(self.gameView)

    def cancel_button(self):
        self.window.show_view(self.priorView)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.W or symbol == arcade.key.UP:
            if self.selected > 0:
                self.selected -= 1

        if symbol == arcade.key.S or symbol == arcade.key.DOWN:
            if self.selected < parameters.NUM_SAVE_FILES:
                self.selected += 1

        if symbol == arcade.key.SPACE:
            if self.selected == parameters.NUM_SAVE_FILES:
                self.cancel_button()
            else:
                self.save_button(self.selected+1) if self.state else self.load_button(self.selected+1)


    def load(self, file):
        array = []
        dbfile = open(f"savefile{file}", 'rb')
        data = pickle.load(dbfile)
        array.append(data["wallet"])
        array.append(data["level"])
        dbfile.close()
        if array[1] == 0:
            array.append("Empty File")
        else:
            array.append(f"File: {file}\t level: {array[1]}\t $: {array[0]}")
        return array