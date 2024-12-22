theboard = {"7":' ' , '8': ' ' , '9': ' ' ,
            "4":' ' , '5': ' ' , '6': ' ' ,
            "1":' ' , '2': ' ' , '3': ' '} 
board_keys = []
for key in theboard:
    board_keys.append(key)
    def printBoard(board):
        print(board['7'] +'|' + board['8'] + '|' board['9'] + '|')
        print('-+-+-')
        print(board['4'] +'|' + board['5'] + '|' board['6'] + '|')
        print('-+-+-')
        print(board['1'] +'|' + board['2'] + '|' board['3'] + '|')

    def game():

        turn = 'x'
        count = 0

        
        for i in range(10):
            printBoard(theboard)
            print("It's you'r turn", + turn + ".Pick a best place")
            continue

        if count >= 5:
            if theboard['7'] == theboard['8'] == theboard['9'] !=' ':#
                printBoard(theboard)
                print(turn, 'vins')
                break
            
            elif theboard['4'] == theboard['5'] == theboard['6'] !=' ':#
                printBoard(theboard)
                print(turn, 'vins')
                break

            elif theboard['1'] == theboard['2'] == theboard['3'] !=' ':#
                printBoard(theboard)
                print(turn, 'vins')
                break

            elif theboard['1'] == theboard['4'] == theboard['7'] !=' ':#
                printBoard(theboard)
                print(turn, 'vins')
                break
            elif theboard['2'] == theboard['5'] == theboard['8'] !=' ':#
                printBoard(theboard)
                print(turn, 'vins')
                break
            elif theboard['3'] == theboard['6'] == theboard['9'] !=' ':#
                printBoard(theboard)
                print(turn, 'vins')
                break
            elif theboard['7'] == theboard['5'] == theboard['3'] !=' ':#
                printBoard(theboard)
                print(turn, 'vins')
                break
            elif theboard['1'] == theboard['5'] == theboard['9'] !=' ':#
                printBoard(theboard)
                print(turn, 'vins')
                break
        if count >9:
            print("\nGame Over.\n")
            print("it's a Tie!!")


        if turn == 'x':
            turn = 0 
        else:
            turn = 'x'

    restart = input("Do you want to play Again?(y/n)")
    if restart == "y" or restart == "y":
        for key in board_keys:
            theboard[key] = " "

        game()
if __name__ == "__main__":
    game()