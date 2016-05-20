################################################################################
#
################################################################################
from game import Game

def main():
	
    game = Game()
    game.playGame()
	continuePlaying = True
	while (continuePlaying):
        if ( game.playNewGame):
			game.resetGame()
	
	
if __name__=="__main__":
        main()
