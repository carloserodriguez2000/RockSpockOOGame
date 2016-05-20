from Choice import Choice

class Player:
   
    def __init__(self, name):
        self.name = name.upper()    #create and empty string to hold name
        self.scores= []
        # choice = None
        
    def takeTurn(self, playerx):
        newChoice = Choice()
        # x= newChoice.getChoice(playerx.name)
        playerx.choice = newChoice.getChoice(playerx.name)
       
   
    
       
