import random

def getInput(theBoard, player):
    if player == 'X':
        remaining_pos = [key for key, value in theBoard.items() if value == ' ']
        get_position = input(f"Remaining positions: {remaining_pos} => ").upper()
        get_value = 'X'
    else:
        # Computer's turn - select a random empty position
        remaining_pos = [key for key, value in theBoard.items() if value == ' ']
        get_position = random.choice(remaining_pos)
        get_value = 'O'
    theBoard[get_position] = get_value

def checker(board):
    # Function to check if any player has won
    if (board['TL'] == board['TM'] == board['TR'] and board['TL'] != ' ') or \
       (board['ML'] == board['MM'] == board['MR'] and board['ML'] != ' ') or \
       (board['LL'] == board['LM'] == board['LR'] and board['LL'] != ' ') or \
       (board['TL'] == board['MM'] == board['LR'] and board['TL'] != ' ') or \
       (board['LL'] == board['MM'] == board['TR'] and board['LL'] != ' ') or \
       (board['TL'] == board['ML'] == board['LL'] and board['TL'] != ' ') or \
       (board['TM'] == board['MM'] == board['LM'] and board['TM'] != ' ') or \
       (board['TR'] == board['MR'] == board['LR'] and board['TR'] != ' '):
        print("----------GAME OVER-----------")
        return True
    else:
        return False

def printBoard(board):
    # Function to print the tic-tac-toe board
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print("-+-+-")
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print("-+-+-")
    print(board['LL'] + '|' + board['LM'] + '|' + board['LR'])

while True:
    theBoard = {'TL': ' ', 'TM': ' ', 'TR': ' ',
                'ML': ' ', 'MM': ' ', 'MR': ' ',
                'LL': ' ', 'LM': ' ', 'LR': ' '}
    playIt = input("Do you want to play Tic-Tac-Toe? (y/n): ").lower()
    if playIt == 'y':
        for i in range(0, 9):  # Maximum 9 moves allowed
            printBoard(theBoard)
            if i % 2 == 0:  # Player's turn
                getInput(theBoard, 'X')
            else:  # Computer's turn
                getInput(theBoard, 'O')
            if i >= 4:  # Check for a winner after 5 moves
                if checker(theBoard):
                    printBoard(theBoard)
                    break
    else:
        print("Thank you for playing!")
        break
