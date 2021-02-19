from random import randint

board = [
    [' ', '|', ' ', '|', ' '],
    ['-', '+', '-', '+', '-'],
    [' ', '|', ' ', '|', ' '],
    ['-', '+', '-', '+', '-'],
    [' ', '|', ' ', '|', ' '],
]

def main():
    game_over = False

    while not game_over:
        cpu_choice = str(randint(1, 9))
        player_choice = input('Choose a position (1-9)\n')

        if not check_board(player_choice):
            print('Invalid move, please select a different position (1-9)\n')
            continue

        if player_choice == cpu_choice or not check_board(cpu_choice):
            while player_choice == cpu_choice or not check_board(cpu_choice):
                cpu_choice = str(randint(1, 9))

        take_turn(player_choice, "human")
        take_turn(cpu_choice, "cpu")

        print_board()

        if check_winner(board, 'X'):
            print('Congratulations! You won!\n')
            game_over = True
        elif check_winner(board, '0'):
            print('Unlucky! The CPU won. Better luck next time...\n')
            game_over = True
        elif check_tie(board):
            print('It was a tie!\n')
            game_over = True


def check_board(choice):
    board_position = {
        '1': board[0][0],
        '2': board[0][2],
        '3': board[0][4],
        '4': board[2][0],
        '5': board[2][2],
        '6': board[2][4],
        '7': board[4][0],
        '8': board[4][2],
        '9': board[4][4],
    }

    if not choice in board_position:
        return False

    if not board_position[choice] == ' ':
        return False
    else:
        return True


def take_turn(choice, player):
    if player == "human":
        symbol = 'X'
    else:
        symbol = '0'

    if choice == '1':
        board[0][0] = symbol
    if choice == '2':
        board[0][2] = symbol
    if choice == '3':
        board[0][4] = symbol
    if choice == '4':
        board[2][0] = symbol
    if choice == '5':
        board[2][2] = symbol
    if choice == '6':
        board[2][4] = symbol
    if choice == '7':
        board[4][0] = symbol
    if choice == '8':
        board[4][2] = symbol
    if choice == '9':
        board[4][4] = symbol
        

def print_board():
    row = ""
    for i in board:
        for j in i:
            row += j
        print(row)
        row = ""


def check_winner(current_board, symbol):
    winning_boards = {
        'row_one': current_board[0][0] == symbol and current_board[0][2] == symbol and current_board[0][4] == symbol,
        'row_two': current_board[2][0] == symbol and current_board[2][2] == symbol and current_board[2][4] == symbol,
        'row_three': current_board[4][0] == symbol and current_board[4][2] == symbol and current_board[4][4] == symbol,
        'col_one': current_board[0][0] == symbol and current_board[2][0] == symbol and current_board[4][0] == symbol,
        'col_two': current_board[0][2] == symbol and current_board[2][2] == symbol and current_board[4][2] == symbol,
        'col_three': current_board[0][4] == symbol and current_board[2][4] == symbol and current_board[4][4] == symbol,
        'back_slash': current_board[0][0] == symbol and current_board[2][2] == symbol and current_board[4][4] == symbol,
        'fwd_slash': current_board[0][4] == symbol and current_board[2][2] == symbol and current_board[4][0] == symbol,
    }

    for i in winning_boards: 
        if winning_boards[i]:
            return True


def check_tie(current_board):
    space_count = 0
    for x in current_board:
        for y in x:
            if y == ' ':
                space_count += 1

    if space_count > 2:
        return False
    else:
        return True 


if __name__ == "__main__":
    main()