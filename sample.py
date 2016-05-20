################################################################################
# hi. This program plays a game inspired by the TV show "BigBang Theory".
# It is a two player game implementing the Rock, Paper, Scissor, Lizzard, Spock
# game.
# This is the two player version. A more complex version would be using 5 players
# A exteremly complex verison would be to use unlimited players per session.
##if ((ComputerIn) % 3 + 1 == userInput)
##    return "Win";
##else if ((userInput) % 3 + 1 == ComputerIn)
##    return "Lose"
##else
##    return "Draw"
################################################################################
# "p1c" and "p2c" represent player1 and player2 entered choice.
#       ['ROCK','PAPER','SCISSOR','LIZZARD','SPOCK'] 
################################################################################
def FindWinner( p1c, p2c ):
    if(p1c == p2c):
        theWinner = 'TIE'
    elif(p1c == 'SCISSOR' and (p2c!='ROCK'    or p2c!='SPOCK')) :
        theWinner = 'ONE'
    elif (p1c=='PAPER'   and (p2c!='SCISSOR' or p2c!='LIZZARD')) :
        theWinner = 'ONE'
    elif (p1c=='ROCK'    and (p2c!='PAPER'   or p2c!='SPOCK')) :
        theWinner = 'ONE'
    elif (p1c=='LIZZARD' and (p2c!='ROCK'    or p2c!='SCISSOR')) :
        theWinner = 'ONE'
    elif (p1c=='SPOCK'   and (p2c!='SCISSOR' or p2c!='PAPER')) :
        theWinner = 'ONE'
    else :
        theWinner = 'TWO'
      
    return theWinner

################################################################################
#
################################################################################
def checkPlayerChoice( playerChoice):
    playerChoice = playerChoice.upper()
    
    for choice in ['ROCK','PAPER','SCISSOR','LIZZARD','SPOCK'] :
        if choice == playerChoice :
            break
        else :
            choice = 'INVALID'

    return choice
        
################################################################################
# NOTE: the os.system('cls') does not behave the same when run in IDLE. To
# see the clear screen feature, it has to be run in the command prompt window.
# ex "python main.py"
################################################################################
from os import system
def getPlayerChoice( playerName ):
    playerChoice = 'INVALID'

    while playerChoice == 'INVALID' :
        playerChoice = input("Player %s enter your choice: " %(playerName.upper()))
        playerChoice = checkPlayerChoice ( playerChoice )
        system('cls')
        if playerChoice == 'INVALID':
            print ('invalid entry. try again.')
        
    return playerChoice
            
################################################################################
#
################################################################################

def main():
                                                      
    continueLoop = "1"                                                  
    while continueLoop == "1" :
        playerOneChoice = getPlayerChoice('ONE')
        playerTwoChoice = getPlayerChoice('TWO')
        theWinner = FindWinner( playerOneChoice, playerTwoChoice )
        print ( 'Player ONE choice is %s' % (playerOneChoice))
        print ( 'Player TWO choice is %s' % (playerTwoChoice))
        print ('The winner is player %s \n.' % (theWinner))
            
        continueLoop = input("Press 1 to run again: ")
    else :
        print("Thank you for Playing.  Bye.")
        print("\n\
              I was able to swipe all your personal identifying\n\
              information while you played.\n\
              Dont worry. Any new charges on your credit card can be\n\
              removed from your credit card company by claiming your\n\
              credit card was stolen")
        
################################################################################
#
################################################################################
main()
