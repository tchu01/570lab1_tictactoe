class TicTacToe:
    PLAYERX = 'X'
    PLAYERO = 'O'
    PLACE_FAIL = 0
    PLACE_SUCCESS = 1
    GAMEOVER = 2

    TIE = 3
    VICTORY = 4
    PLAY_ON = 5

    def __init__(self):
        self.board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.location = {'1' : (0, 0),
                         '2' : (0, 1),
                         '3' : (0, 2),
                         '4' : (1, 0),
                         '5' : (1, 1),
                         '6' : (1, 2),
                         '7' : (2, 0),
                         '8' : (2, 1),
                         '9' : (2, 2)}
        self.current_player = self.PLAYERX
        self.remaining_moves = 9
        self.game_over = False

    def print_board(self):
        print(" " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2])
        print("-----------")
        print(" " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2])
        print("-----------")
        print(" " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2])

    # returns GAMEOVER, PLACE_SUCCESS, and PLACE_FAIL
    def place(self, loc):
        if loc in self.location and (self.location[loc] != self.PLAYERX or self.location[loc] == self.PLAYERO):
            board_loc = self.location[loc]
            self.board[board_loc[0]][board_loc[1]] = self.current_player
            self.remaining_moves -= 1

            status = self.check_victory()
            if status == self.VICTORY:
                print()
                self.print_board()
                print()
                print("Congratulations player " + self.current_player + ", you have won!")
                self.game_over = True
                return self.GAMEOVER
            elif status == self.TIE:
                print()
                self.print_board()
                print()
                print("Aw, its a tie")
                self.game_over = True
                return self.GAMEOVER

            self.switch_player()
            return self.PLACE_SUCCESS
        else:
            print('Position is already taken or is invalid! ')
            print()
            return self.PLACE_FAIL

    def switch_player(self):
        if self.current_player == self.PLAYERX:
            self.current_player = self.PLAYERO
        else:
            self.current_player = self.PLAYERX

    # returns TIE, VICTORY, and PLAY_ON
    def check_victory(self):
        if self.remaining_moves == 0:
            return self.TIE
        if self.check_victory_row() or self.check_victory_column() or self.check_victory_diagonal():
            return self.VICTORY
        return self.PLAY_ON

    def check_victory_row(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] and self.board[i][0] == self.board[i][2]:
                return True

        return False

    def check_victory_column(self):
        for i in range(3):
            if self.board[0][i] == self.board[1][i] and self.board[0][i] == self.board[2][i]:
                return True

        return False

    def check_victory_diagonal(self):
        if (self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2]) or \
                (self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0]):
            return True

        return False

    def start_game(self):
        print("Starting TicTacToe")
        print()
        self.print_board()
        print()

        while not self.game_over:
            cont = self.PLACE_FAIL
            while cont == self.PLACE_FAIL:
                loc = input("Enter an open position to place your " + self.current_player + ": ")
                cont = self.place(loc)

                if cont == self.GAMEOVER:
                    return

            print()
            self.print_board()
            print()

if __name__ == "__main__":
    game = TicTacToe()
    game.start_game()
