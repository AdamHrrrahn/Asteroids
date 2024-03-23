import arcade
from GameView import GameView
from StationView import StationView
from PauseView import PauseView
from PlayerShip import PlayerShip
from UpgradeView import UpgradeView
from IntroView import IntroView
from DeathView import DeathView
from save_loadView import save_loadView
import parameters



if __name__ == "__main__":
    window = arcade.Window(parameters.SCREEN_WIDTH, parameters.SCREEN_HEIGHT, parameters.SCREEN_TITLE)
    player = PlayerShip("sprites/PlayerShip/tile000.png", parameters.SCALING)
    player.setUp()
    gameView = GameView(player)
    pauseView = PauseView()
    stationView = StationView()
    upgradeView = UpgradeView()
    introView = IntroView()
    deathView = DeathView()
    saveView = save_loadView()
    saveView.setViews(gameView, player)
    introView.setViews(gameView, saveView, player)
    gameView.setViews(pauseView, stationView, deathView)
    pauseView.setViews(gameView)
    stationView.setViews(gameView, player, upgradeView, saveView)
    upgradeView.setViews(stationView, player)
    deathView.setViews(introView)
    window.show_view(introView)
    # app = Game()
    
    arcade.run()