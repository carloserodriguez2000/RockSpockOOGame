from Player import Player

class ScoreBoard:
    def __init__(self, player1, player2):
        #    self.scores = [[],[]]
        self.scores = {str(player1.name):0, str(player2.name):0}
        self.playerIndex = {str(player1.name): 0 ,str(player2.name):0}
        self.totals = {str(player1.name):0 ,str(player2.name):0}

    def storeScore(self, winner):
        self.scores.append([winner])  # these should be 0 or 1 depending who won the round
        print('scores array is: ', self.scores)
        
    def printScores(self):
        i=4
        
    def printScore(player):
        print("%s your score is %s" %(player.name, player.score))
        
        
    def gameWinner(self,player1, player2):
        self.tallyScore(player1, player2)
        hi = player1.name
        if self.totals[player1.name]> self.totals[player2] :
            print('The winner is %s.' %(player1.name))
            print('The Totals are', self.totals)
        else:
            print('The winner is %s.' %(player2.name))
            print('The Totals are', self.totals)
       
    
    
    def tallyScore( self, player1, player2):
        self.totals[player1.name] = 5
        self.totals[player2.name] = 7
        self.scores['toni']= 8
        self.scores['mike']=10
        print(self.scores)
        print(self.totals)
        score = self.scores['toni']
        print ( score)
        score = self.scores[player1.name]
        print ( score)
        for score in self.scores[player1.name]:
            print (score)
            self.totals[player1.name]+= score
       
        for score in self.scores:
            print (score)
            self.totals[player1.name]+= score[player1.name]
            self.totals[player2.name]+= score[player2.name]
            
        print('Player totals: ', self.totals)
        return
    
    