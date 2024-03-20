import arcade
from GameView import GameView
from StationView import StationView
from PauseView import PauseView
from PlayerShip import PlayerShip
from UpgradeView import UpgradeView
from IntroView import IntroView
import parameters



if __name__ == "__main__":
    window = arcade.Window(parameters.SCREEN_WIDTH, parameters.SCREEN_HEIGHT, parameters.SCREEN_TITLE)
    player = PlayerShip("sprites/PlayerShip/tile000.png", parameters.SCALING)
    gameView = GameView(player)
    pauseView = PauseView()
    stationView = StationView()
    upgradeView = UpgradeView()
    introView = IntroView()
    introView.setViews(gameView)
    gameView.setViews(pauseView, stationView)
    pauseView.setViews(gameView)
    stationView.setViews(gameView, player, upgradeView)
    upgradeView.setViews(stationView, player)
    window.show_view(introView)
    # app = Game()
    
    arcade.run()