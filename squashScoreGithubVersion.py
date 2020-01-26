from tkinter import Tk, Label, Button, Grid, StringVar, N, S, E, W, OptionMenu
import time
import csv
import datetime

# Variable Declarations

currentDate = datetime.datetime.now().strftime('%A')

Players = [
'Player1',
'Player2',
'Player3',
'Player4',
'Player5'
]

master = Tk()

gameData = []
matchData = []

currentGame = 1
currentMatch = 1
playerOneScore = 0
playerTwoScore = 0

Grid.columnconfigure(master, 0, weight=1)
Grid.columnconfigure(master, 1, weight=1)

playerOneVariable = StringVar(master)
playerOneVariable.set('Please Select')

playerTwoVariable = StringVar(master)
playerTwoVariable.set('Please Select')

# Function Declarations
def confirm():
    if playerOneVariable.get() != 'Please Select':
        print ("value is:" + playerOneVariable.get())
    else:
        print('Please select a value')

def updatePlayerOneButton():
    playerOneButton.configure(text = f'Point to {playerOneVariable.get()}')
    playerOneButton.after(100, updatePlayerOneButton)

def updatePlayerTwoButton():
    playerTwoButton.configure(text = f'Point to {playerTwoVariable.get()}')
    playerTwoButton.after(100, updatePlayerTwoButton)

def updatePlayerOneScore():
    global playerOneScore
    global playerTwoScore

    if playerOneVariable.get() == 'Please Select' or playerTwoVariable.get() == 'Please Select':
        print('please select the players')
    elif playerOneVariable.get() == playerTwoVariable.get():
        print('please select two different players')
    else:
        if playerOneScore >= 11 and not (abs(playerOneScore - playerTwoScore) < 2):
            print('Player One Wins')
        elif playerTwoScore >= 11 and not (abs(playerOneScore - playerTwoScore) < 2):
            print('Player Two has won')
        else:
            playerOneScore += 1

            if not gameData:
                gameData.append([playerOneVariable.get(), playerTwoVariable.get()])
                gameData.append([playerOneScore, playerTwoScore])           
            else:
                gameData.append([playerOneScore, playerTwoScore])

def updatePlayerTwoScore():
    global playerTwoScore
    global playerOneScore

    if (playerOneVariable.get == 'Please Select' or playerTwoVariable.get() == 'Please Select'):
        print('please select the players')
    elif playerOneVariable.get() == playerTwoVariable.get():
        print('please select two different players')
    else:
        if playerTwoScore >= 11 and not (abs(playerOneScore - playerTwoScore) < 2):
            print('Player Two Wins')
        elif playerOneScore >= 11 and not (abs(playerOneScore - playerTwoScore) < 2):
            print('Player One has won')
        else:
            playerTwoScore += 1

            if not gameData:
                gameData.append([playerOneVariable.get(), playerTwoVariable.get()]) 
                gameData.append([playerOneScore, playerTwoScore])                     
            else:
                gameData.append([playerOneScore, playerTwoScore])

def updateScoreLabel():
    scoreLabel.configure(text = f'{playerOneScore} : {playerTwoScore}')
    scoreLabel.after(100, updateScoreLabel)

def restartGame():
    global playerOneScore
    global playerTwoScore
    global gameData
    global currentGame
    global matchData

    playerOneScore = 0
    playerTwoScore = 0
    currentGame += 1

    for row in gameData:
        matchData.append(row)
    
    gameData = []

def restartMatch():
    global playerOneScore
    global playerTwoScore
    global matchData
    global currentGame
    global gameData
    global currentMatch

    playerOneScore = 0
    playerTwoScore = 0

    if gameData:
        for row in gameData:
            matchData.append(row)

    for row in matchData:
        print(row)

    with open(f'{currentDate}_Match_{currentMatch}.csv', 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(matchData)

    matchData = []
    gameData = []
    currentMatch += 1

def exitClient():
    exit()

# Main program start
Label(master, text = 'Overall Score: ', justify = 'center', font = (None, 15)).grid(row = 0, column = 0, columnspan = 2, sticky=N+S+E+W)
scoreLabel = Label(master, font = (None, 30))
scoreLabel.grid(row = 1, column = 0, columnspan = 2, sticky=N+S+E+W)
updateScoreLabel() # runs update score label function

Label(master, text = 'Player One Select').grid(row = 2, column = 0, sticky=N+S+E+W) # Player One Select text
OptionMenu(master, playerOneVariable, *Players).grid(row = 3, column = 0, sticky=E+W, pady = (0, 10)) # Player One Select Dropdown

Label(master, text = 'Player Two Select').grid(row = 2, column = 1, sticky=N+S+E+W) # Player Two Select text
OptionMenu(master, playerTwoVariable, *Players).grid(row = 3, column = 1, sticky=E+W, pady = (0, 10)) # Player One Select Dropdown

playerOneButton = Button(master, command = updatePlayerOneScore)
playerOneButton.grid(row = 4, column = 0, sticky=N+S+E+W, pady = (0, 10)) # Button to give points to player one
updatePlayerOneButton()

playerTwoButton = Button(master, command = updatePlayerTwoScore)
playerTwoButton.grid(row = 4, column = 1, sticky=N+S+E+W, pady = (0, 10)) # Button to give points to player two
updatePlayerTwoButton()

Button(master, text = 'Exit', command = exitClient).grid(row = 6, column = 0, columnspan = 2, sticky=E+W, pady = (0, 10)) # Exit button

Button(master, text = 'New Game', command = restartGame).grid(row = 5, column = 0, sticky=E+W, pady = (0, 10)) # New Game button
Button(master, text = 'Save Match', command = restartMatch).grid(row = 5, column = 1, sticky=E+W, pady = (0, 10)) # New Game button


master.title('Squash Score Client')
master.geometry('500x300')

master.mainloop()