"""
Name(s):Neel and max
Name of Project: Connect 4 
"""

board = [['•','•','•','•','•','•','•'],['•','•','•','•','•','•','•'],['•','•','•','•','•','•','•'],['•','•','•','•','•','•','•'],['•','•','•','•','•','•','•'],['•','•','•','•','•','•','•']]
players = ['','']
def print_board():
    '''Prints the current state of the board.'''
    print('\n')
    print(' 0 1 2 3 4 5 6 ')
    for rows in board:
        row = ''
        for item in rows:
            row += item
            row += ' '
        row = row.strip(' ')
        print('[' + row + ']')

def set_up_game():
    '''set_up_game() -> list
    returns a list of players' names'''
    playerList = []  # initialize list of players
    # get player data
    name = input("Player " + 'X' + ", enter your name: ")
    playerList.append(name)
    name = input("Player " + 'O' + ", enter your name: ")
    playerList.append(name)
    #print(playerList)
    players[0] = playerList[0]
    players[1] = playerList[1]
    return playerList
#set_up_game()
def play_game():
    '''Plays a game of connect 4.'''
    boardFull = 0
    set_up_game()
    playerTurn = 0
    print_board()
    while True:
        columnToPlay = -1
        userInput = '-1'

        #userInput = input('Choose a column to play in: (Pick a number from 0 to 6)')

        while True:
            try:
                print(players[playerTurn] + ", it's your turn.")
                userInput = input('Choose a column to play in: (Pick a number from 0 to 6)')
                columnToPlay = int(userInput)
            except:
                print("Input an integer from 0 to 6.")
                continue

            if 0 <= columnToPlay <= 6:
                  break

        # print(columnToPlay)
        for rows in range(6):
          for cols in range(7):
            if board[rows][cols] in ['X','O']:
              boardFull += 1
            else:
              boardFull = 0
        if boardFull != 42:
          boardFull = 0
        for i in reversed(range(6)):
            if board[i][columnToPlay] == '•':
                if playerTurn == 0:
                    board[i][columnToPlay] = 'X'
                    playerTurn = 1
                    break
                else:
                    board[i][columnToPlay] = 'O'
                    playerTurn = 0
                    break
        print_board()
        for rowIn in range(6):
            for col in range(7):
                row = board[rowIn]
                column = [board[0][col],board[1][col],board[2][col],board[3][col],board[4][col],board[5][col]]
                if rowIn <= 2:
                    next1Row = board[rowIn+1]
                    next2Row = board[rowIn+2]
                    next3Row = board[rowIn+3]
                # check horizontally
                if col <= 3 and row[col] == row[col+1] == row[col+2] == row[col+3] and (row[col] in ['X','O']):
                    if playerTurn == 0:
                        print(players[1] + ' has won the game!')
                    else:
                        print(players[0] + ' has won the game!')
                    return players[playerTurn]
                elif rowIn <= 2 and column[rowIn] == column[rowIn + 1] == column[rowIn + 2] == column[rowIn + 3] and (column[rowIn] in ['X','O']):
                    if playerTurn == 0:
                        print(players[1] + ' has won the game!')
                    else:
                        print(players[0] + ' has won the game!')
                    return players[playerTurn]
                elif col <= 3 and rowIn <= 2 and row[col] == next1Row[col + 1] == next2Row[col + 2] == next3Row[col + 3] and (row[col] in ['X','O']):
                    if playerTurn == 0:
                        print(players[1] + ' has won the game!')
                    else:
                        print(players[0] + ' has won the game!')
                    return players[playerTurn]
                elif col >= 3 and rowIn <= 2 and row[col] == next1Row[col-1] == next2Row[col-2] == next3Row[col-3] and (row[col] in ['X','O']):
                    if playerTurn == 0:
                        print(players[1] + ' has won the game!')
                    else:
                        print(players[0] + ' has won the game!')
                    return players[playerTurn]
                elif boardFull == 42:
                  print("It's a tie!")
                  return

play_game()





#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
