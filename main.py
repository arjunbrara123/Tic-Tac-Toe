dMap = {
    "a1": "-",
    "a2": "-",
    "a3": "-",
    "b1": "-",
    "b2": "-",
    "b3": "-",
    "c1": "-",
    "c2": "-",
    "c3": "-"
}


def get_board():
    return f"""   a     b     c
      |     |     
1  {dMap['a1']}  |  {dMap['b1']}  |  {dMap['c1']}  
 _____|_____|_____
      |     |     
2  {dMap['a2']}  |  {dMap['b2']}  |  {dMap['c2']}  
 _____|_____|_____
      |     |     
3  {dMap['a3']}  |  {dMap['b3']}  |  {dMap['c3']}  
      |     |     """


def checkWin() -> str:
    if dMap['a1'] == "x" and dMap['b1'] == "x" and dMap['c1'] == "x":
        return "Player 1 Wins!"
    elif dMap['a2'] == "x" and dMap['b2'] == "x" and dMap['c2'] == "x":
        return "Player 1 Wins!"
    elif dMap['a3'] == "x" and dMap['b3'] == "x" and dMap['c3'] == "x":
        return "Player 1 Wins!"
    elif dMap['a1'] == "x" and dMap['a2'] == "x" and dMap['a3'] == "x":
        return "Player 1 Wins!"
    elif dMap['b1'] == "x" and dMap['b2'] == "x" and dMap['b3'] == "x":
        return "Player 1 Wins!"
    elif dMap['c1'] == "x" and dMap['c2'] == "x" and dMap['c3'] == "x":
        return "Player 1 Wins!"
    elif dMap['a1'] == "x" and dMap['b2'] == "x" and dMap['c3'] == "x":
        return "Player 1 Wins!"
    elif dMap['a3'] == "x" and dMap['b2'] == "x" and dMap['c1'] == "x":
        return "Player 1 Wins!"
    elif dMap['a1'] == "o" and dMap['b1'] == "o" and dMap['c1'] == "o":
        return "Player 2 Wins!"
    elif dMap['a2'] == "o" and dMap['b2'] == "o" and dMap['c2'] == "o":
        return "Player 2 Wins!"
    elif dMap['a3'] == "o" and dMap['b3'] == "o" and dMap['c3'] == "o":
        return "Player 2 Wins!"
    elif dMap['a1'] == "o" and dMap['a2'] == "o" and dMap['a3'] == "o":
        return "Player 2 Wins!"
    elif dMap['b1'] == "o" and dMap['b2'] == "o" and dMap['b3'] == "o":
        return "Player 2 Wins!"
    elif dMap['c1'] == "o" and dMap['c2'] == "o" and dMap['c3'] == "o":
        return "Player 2 Wins!"
    elif dMap['a1'] == "o" and dMap['b2'] == "o" and dMap['c3'] == "o":
        return "Player 2 Wins!"
    elif dMap['a3'] == "o" and dMap['b2'] == "o" and dMap['c1'] == "o":
        return "Player 2 Wins!"

    if "-" not in dMap.values():
        return "No more move possible... Game is a Draw!"
    else:
        return ""


# Initialise game variables
player_turn = 2
check_winner = ""

# Show initial board
print(get_board())

while check_winner == "":

    # Next Player Turn
    if player_turn == 1:
        player_turn = 2
    elif player_turn == 2:
        player_turn = 1

    # Ask user to move

    move = input(f"Player {player_turn} Move: ").lower()

    # Make if valid move
    if move in dMap.keys():
        if dMap[move] == "-":
            if player_turn == 1:
                dMap[move] = "x"
            elif player_turn == 2:
                dMap[move] = "o"
        else:
            print("Piece already there... Switching Player... =P")
    else:
        print("Invalid move... Switching Player =P")

    # Show board after move
    print(get_board())

    # Check for winner
    check_winner = checkWin()

print(checkWin())
print("Game Over!")
