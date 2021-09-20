
moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
# Output: "A"


def tictactoe(moves):
    N = 3
    rows, cols = [0] * N, [0] * N
    mainDiag = antiDiag = 0

    player = 1
    for r, c in moves:
        rows[r] += player
        cols[c] += player
        if r == c: mainDiag += player
        if r + c == N - 1: antiDiag += player
        if abs(rows[r]) == N or abs(cols[c]) == N or abs(mainDiag) == N or abs(antiDiag) == N:
            return "A" if player == 1 else "B"
        player = -player

    return "Draw" if len(moves) == N * N else "Pending"



print(tictactoe(moves))