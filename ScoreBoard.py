from Player import Player

class ScoreBoard:
    def __init__(self, player1, player2):
        self.playerIndex = {str(player1.name): 0 ,str(player2.name):1}
        self.totals=[[],[]]

    def storeScore(self, winner,player1, player2):
        if (player1.name==winner):
            player1.scores.append(1)
        else:
            player2.scores.append(1)
        
    def printScores(self,playerx):
        i=4
        print( playerx.scores)
        
    def printScore(player):
        print("%s your score is %s" %(player.name, player.score))

        
        
    def printRoundWinner ( self, winnerName, player1, player2):
        print('This Round Winner is %s.\n' %(winnerName))
            
            
    def gameWinner(self,player1, player2):
        player1Index=self.playerIndex[player1.name]
        player2Index= self.playerIndex[player2.name]
        self.tallyScore(player1, player2)
        
        if self.totals[player1Index]> self.totals[player2Index] :
            print('The winner is %s.' %(player1.name))
            print('The Totals are', self.totals)
        else:
            print('The winner is %s.' %(player2.name))
            print('The Totals are', self.totals)
       
    
    
    def tallyScore( self, player1, player2):
        player1Index=self.playerIndex[player1.name]
        player2Index= self.playerIndex[player2.name]
        self.totals[player1Index] = 5
        self.totals[player2Index] = 7
        # print(self.scores)
        print(self.totals)
        # score = self.scores['toni']
        # print ( score)
        # score = self.scores[player1.name]
        print ( player1.scores)
        print ( player2.scores)

        for score in player1.scores:
            print (score)
            self.totals[player1Index]+= score
            
        for score in player2.scores:
            print (score)
            self.totals[player2Index]+= score
  
            
        print('Player totals: ', self.totals)
        return
    
    