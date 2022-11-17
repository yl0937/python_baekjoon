n, m = map(int, input().split())
board = []
mini_board = []

for _ in range(n):
    board.append(input())

for row in range(n - 7):
    for column in range(m - 7):
        white_start = 0
        black_start = 0
        for b in range(row, row + 8):
            for j in range(column, column + 8):
                if (b + j) % 2 == 0:
                    if board[b][j] != 'W':
                        white_start += 1
                    elif board[b][j] != 'B':
                        black_start += 1
                else:
                    if board[b][j] != 'B':
                        white_start += 1
                    elif board[b][j] != 'W':
                        black_start += 1
        mini_board.append(white_start)
        mini_board.append(black_start)

print(min(mini_board))