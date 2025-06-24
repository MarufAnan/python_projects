import math

# Initialize board
board = [" " for _ in range(9)]
player = "X"
ai = "O"

def print_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")

def get_winner(b):
    win_patterns = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for a, b1, c in win_patterns:
        if b[a] != " " and b[a] == b[b1] and b[a] == b[c]:
            return b[a]
    return "Draw" if " " not in b else None

def minimax(new_board, current_player):
    winner = get_winner(new_board)
    if winner == player:
        return {"score": -10}
    elif winner == ai:
        return {"score": 10}
    elif " " not in new_board:
        return {"score": 0}

    moves = []

    for i in range(9):
        if new_board[i] == " ":
            move = {}
            move["index"] = i
            new_board[i] = current_player

            result = minimax(new_board, ai if current_player == player else player)
            move["score"] = result["score"]

            new_board[i] = " "
            moves.append(move)

    if current_player == ai:
        best_score = -math.inf
        best_move = None
        for move in moves:
            if move["score"] > best_score:
                best_score = move["score"]
                best_move = move
    else:
        best_score = math.inf
        best_move = None
        for move in moves:
            if move["score"] < best_score:
                best_score = move["score"]
                best_move = move

    return best_move

def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == " ":
                board[move] = player
                break
            else:
                print("Invalid move. Try again.")
        except:
            print("Please enter a number between 1 and 9.")

def ai_move():
    move = minimax(board, ai)["index"]
    board[move] = ai
    print(f"AI chooses position {move + 1}")

# Game loop
print("Tic Tac Toe (You = X, AI = O)")
print_board()

while True:
    player_move()
    print_board()
    result = get_winner(board)
    if result:
        print("Draw!" if result == "Draw" else f"{result} wins!")
        break

    ai_move()
    print_board()
    result = get_winner(board)
    if result:
        print("Draw!" if result == "Draw" else f"{result} wins!")
        break
