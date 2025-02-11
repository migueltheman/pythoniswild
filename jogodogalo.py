# jogo feito pela equipa Arnaldo Badalhoca

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Verificar linhas, colunas e diagonais
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        try:
            col = int(input(f"Jogador {current_player}, insira a coluna (0, 1, 2): "))
            row = int(input(f"Jogador {current_player}, insira a linha (0, 1, 2): "))
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Já agora continua até ao infinito e mais além")
                continue
        except ValueError:
            print("Já agora continua até ao infinito e mais além")
            continue

        if board[row][col] != " ":
            print("Deves mesmo achar que és esperto, não é? Jogar fora da grelha não é permitido!")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Que lindo, {current_player} ganhou um par de chinelos!")
            break

        if is_full(board):
            print_board(board)
            print("Bom era se alguém ganhasse, mas não foi o caso. Empate!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()