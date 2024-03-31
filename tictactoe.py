def getInput(theBoard):
    remaining_pos=[]
    for key in theBoard.keys():
        if theBoard[key]==' ':
            remaining_pos.append(str(key))
    get_position=input(f"remaining position:+{str(remaining_pos)}=>").upper()
    get_value=input("enter either 'o' or 'x':->")
    theBoard[get_position]=get_value

def checker(board):
    if board['TL']==board['TM']==board['TR'] and board['TL'] !=' ' or  \
        board['ML']==board['MM']==board['MR'] and board['ML'] !=' ' or \
        board['LL']==board['LM']==board['LR'] and board['LL'] !=' ' or \
        board['TL']==board['MM']==board['LR'] and board['TL'] !=' ' or \
        board['LL']==board['MM']==board['TR'] and board['LL'] !=' ' or \
        board['TL']==board['ML']==board['LL'] and board['TL'] !=' ' or \
        board['TM']==board['MM']==board['LM'] and board['TM'] !=' ' or \
        board['TR']==board['MR']==board['LR'] and board['TR'] !=' ':


        print("----------GAME OVER-----------")
        return True
    else: return False



def printBoard(board):
    print(board['TL']+'|'+board['TM']+'|'+board['TR'])
    print("-+-+-")
    print(board['ML']+'|'+board['MM']+'|'+board['MR'])
    print("-+-+-")
    print(board['LL']+'|'+board['LM']+'|'+board['LR'])

while True:
    theBoard = {'TL': ' ', 'TM': ' ', 'TR': ' ',
            'ML': ' ', 'MM': ' ', 'MR': ' ',
            'LL': ' ', 'LM': ' ', 'LR': ' '}
    playIt=input("you wanna play Tic-Tac-Toe(y/n)?:")
    if playIt=='y':
        for i in range(0,10):
            printBoard(theBoard)
            getInput(theBoard)
            if i>=4:
                if checker(theBoard):
                    printBoard(theBoard)
                    break


    else:
        print("Thank You!!")
        break
