import random

# initialize the game board
board = [' ' for _ in range(100)]

# map letters to column indices
col_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}

# place the ships
def place_ships():
    for length in [3, 4]:
        while True:
            # randomly select a starting position and direction
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            direction = random.choice(['horizontal', 'vertical'])
            if direction == 'horizontal' and col + length <= 10:
                # check if the positions are valid
                valid = True
                for c in range(col, col + length):
                    if board[row * 10 + c] != ' ':
                        valid = False
                        break
                if valid:
                    # place the ship on the board
                    for c in range(col, col + length):
                        board[row * 10 + c] = 'S'
                    break
            elif direction == 'vertical' and row + length <= 10:
                # check if the positions are valid
                valid = True
                for r in range(row, row + length):
                    if board[r * 10 + col] != ' ':
                        valid = False
                        break
                if valid:
                    # place the ship on the board
                    for r in range(row, row + length):
                        board[r * 10 + col] = 'S'
                    break

# display the game board
def display_board():
    print('   A B C D E F G H I J')
    for i in range(10):
        print(f'{i}  {" ".join(board[i*10:i*10+10])}')

# play the game
def play_game():
    place_ships()
    display_board()
    num_guesses = 0
    attacked = set()
    while True:
        guess = input('Enter a coordinate to attack (e.g., A3): ')
        if len(guess) != 2:
            print('Invalid coordinate. Please try again.')
            continue
        col = col_map.get(guess[0].upper())
        row = int(guess[1])
        if col is None or row < 0 or row > 9:
            print('Invalid coordinate. Please try again.')
            continue
        index = row * 10 + col
        if index in attacked:
            print('You already attacked that coordinate. Please try again.')
            continue
        attacked.add(index)
        num_guesses += 1
        try:
            if board[index] == 'S':
                board[index] = 'X'
                print('Hit!')
            else:
                board[index] = 'O'
                print('Miss!')
        except IndexError:
            print('An unexpected error occurred. Please try again.')
        display_board()

        # check if the game is over
        if 'S' not in board:
            print('Congratulations! You sunk all the battleships!')
            print('Number of guesses:', num_guesses)
            break
