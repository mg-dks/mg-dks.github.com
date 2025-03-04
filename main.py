class GoBoard:
    def __init__(self, size=9):
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def place_stone(self, x, y, color):
        if self.board[x][y] == '.':
            self.board[x][y] = color
        else:
            print("Invalid move")

def main():
    board = GoBoard()
    board.print_board()
    board.place_stone(3, 3, 'B')
    board.place_stone(16, 16, 'W')
    print("\nAfter placing stones:")
    board.print_board()

if __name__ == "__main__":
    main()
