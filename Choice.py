class Choice:
   
    def __init__(self):
        self.choices = {'ROCK':1, 'PAPER':2, 'SCICCORS':3, 'LIZZARD':4, 'SPOCK':5}
    
           
    def validChoice(self, playerChoice):
        result = playerChoice in self.choices
        print ( playerChoice)
        print ( result)
        return playerChoice in self.choices
    
    def getChoice(self, playerName):
        choice = input("%s enter your choice" % (playerName))
        choice = choice.upper()
        if ( self.validChoice(choice) == True):
            return choice