def countValidChessMoves(board):
    moves = 0

    def isValid(x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def countMoves(x, y, move_offsets, max_steps):
        local_moves = 0
        for dx, dy in move_offsets:
            nx, ny = x, y
            for _ in range(max_steps):
                nx, ny = nx + dx, ny + dy
                if isValid(nx, ny):
                    if board[nx][ny] == '-':
                        local_moves += 1
                    else:
                        break
                else:
                    break
        return local_moves

    def countKingMoves(x, y):
        move_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        return countMoves(x, y, move_offsets, 1)

    def countQueenMoves(x, y):
        move_offsets = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        return countMoves(x, y, move_offsets, 8)

    def countRookMoves(x, y):
        move_offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        return countMoves(x, y, move_offsets, 8)

    def countBishopMoves(x, y):
        move_offsets = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        return countMoves(x, y, move_offsets, 8)

    def countKnightMoves(x, y):
        move_offsets = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        return countMoves(x, y, move_offsets, 1)

    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece == 'K':
                moves += countKingMoves(i, j)
            elif piece == 'Q':
                moves += countQueenMoves(i, j)
            elif piece == 'R':
                moves += countRookMoves(i, j)
            elif piece == 'B':
                moves += countBishopMoves(i, j)
            elif piece == 'N':
                moves += countKnightMoves(i, j)

    return moves

#Testing code provided in main():
def main():
    # update this path with the path to your tests directory !
    testDir = "C:\\Users\\clubb\\OneDrive\\Desktop\\2910\\W4testcases\\" # update this path with the path to your tests directory!
    for i in range(1, 9):  # iterates over test files
        board = []
        numMoves = 0
        with open(f"{testDir}\\board{i}.txt") as idFile:
            for idx, line in enumerate(idFile.readlines()):
                if idx == 8:
                    numMoves = int(line)
                    break
                row = []
                for char in str(line).split()[0]:
                    row.append(char)
                board.append(row)
        print(board)
        calculatedMoves = countValidChessMoves(board)
        if numMoves == calculatedMoves:
            print("Passed")
        else:
            print(f"Failed, Expected: {numMoves}, Got: {calculatedMoves}")
    return 0

if __name__ == '__main__':
    main()
