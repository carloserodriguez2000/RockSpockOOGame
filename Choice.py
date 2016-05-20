class Choice:
   
    def __init__(self):
        self.choices = {'ROCK':1, 'PAPER':2, 'SCICCORS':3, 'LIZZARD':4, 'SPOCK':5}
    
           
    def validChoice(self, playerChoice):
        result = playerChoice in self.choices
        # print ( playerChoice)
        # print ( result)
        return result
    
    def getChoice(self, playerName):
        validFlag = False
        while validFlag == False:
            choice = input("%s     Enter your choice!:  " % (playerName))
            choice = choice.upper()
            if ( self.validChoice(choice) == True):
                print("%s    your choice is!: %s \n" % (playerName, choice))
                print( choice, ' is a great choice.\n')
                validFlag = True
            else:
                validFlag = False
        return choice            