from ScoreBoard import    ScoreBoard
from Player import Player


class Game:
    def ___init___(self):
        # do someting
        i=0

        
    def playGame(self):
        self.player1 = self.getNewPlayer()
        self.player2 = self.getNewPlayer()  # instance of player an store name
        self.scoreBoard = ScoreBoard(self.player1,self.player2)
       
       
        while self.continueGame() == True:
            self.takeTurn(self.player1)
            self.takeTurn(self.player2)
            name = self.checkWinner ( self.player1, self.player2)
            self.scoreBoard.storeScore(name)
            self.scoreBoard.printWinner ( player1, player2)
        
        self.scoreBoard.gameWinner(self.player1,self.player2)
        return False
            
    
    def continueGame(self):
        continueFlag = input('Do you want another round?y/n: ')
        continueFlag= continueFlag.lower()
        if continueFlag == 'y' :
            return True
        else: 
            return False
          
        
    def takeTurn(self, player):
        #DO SOMETHING
        player.takeTurn( player)
        return
   
    def getNewPlayer(self):
       name = input("What is the name of this player: ")
       player = Player(name)
       return player
       
    def playNewGame(self):
        playAgain = input("Does %s and %s want to play a new game? y/n:" %(player1.name, player2.name))
        if( playAgain == 'y'):
            return True
        else:
            return False
    
    def newGame(self):
        #DO SOMETHING
        #erase scores
        # ERASE PLAYERS
        i=0
    def resetGame(self):    #erase players.
        i=0
        # ERASE ALL SCORES
		
    ###############################################################################                
    def checkWinner(self,player1, player2):
        player1Choice = player1.choice
        player2Choice = player2.choice
        
        if(player1Choice == player2Choice):
            theWinner = ''
        elif(player1Choice == 'SCISSOR' and (player2!='ROCK'    or player2!='SPOCK')) :
            theWinner = self.player1.name
        elif (player1Choice=='PAPER'    and (player2!='SCISSOR' or player2!='LIZZARD')) :
            theWinner = self.player1.name
        elif (player1Choice=='ROCK'     and (player2!='PAPER'   or player2!='SPOCK')) :
            theWinner = self.player1.name
        elif (player1Choice=='LIZZARD'  and (player2!='ROCK'    or player2!='SCISSOR')) :
            theWinner = self.player1.name
        elif (player1Choice=='SPOCK'    and (player2!='SCISSOR' or player2!='PAPER')) :
            theWinner = self.player1.name
        else :
            theWinner = self.player2.name
      
        return theWinner
