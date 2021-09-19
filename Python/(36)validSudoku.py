
board = \
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def isValidSudoku(board) -> bool:
    for row in range(9):
        temp_d = {}
        for column in range(9):
            if board[row][column] == '.':
                continue
            elif 1 <= int(board[row][column]) <= 9:
                temp_d.setdefault(board[row][column], 0)
                temp_d[board[row][column]] += 1
            else:
                return False
        print(f"Row {row} temp_d = {temp_d}")
        for v in temp_d.values():
            if v > 1:
                return False
            
    for column in range(9):
        temp_d = {}
        for row in range(9):
            if board[row][column] == '.':
                continue
            elif 1 <= int(board[row][column]) <= 9:
                temp_d.setdefault(board[row][column], 0)
                temp_d[board[row][column]] += 1
            else:
                return False
        print(f"Column {column} temp_d = {temp_d}")
        for v in temp_d.values():
            if v > 1:
                return False
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            temp_d = {}
            for row in board[i:i+3]:
                for num in row[j:j+3]:
                    if num == '.':
                        continue
                    elif 1 <= int(num) <= 9:
                        temp_d.setdefault(num, 0)
                        temp_d[num] += 1
                    else:
                        return False
            print(f"Box row {i} col {j} temp_d = {temp_d}")
            for v in temp_d.values():
                if v > 1:
                    return False
    return True


                
    
print(isValidSudoku(board))

