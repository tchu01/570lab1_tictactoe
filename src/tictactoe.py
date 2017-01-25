import copy
import math

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
        '''
        Prints the current game state's board.
        '''

        print(" " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2])
        print("-----------")
        print(" " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2])
        print("-----------")
        print(" " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2])

    def place(self, loc):
        '''
        Places the mark on the current game state's board.
        If game resulted in victory, prints victor.
        If game resulted in tie, prints tie.
        In both games, self.game_over is set to True.


        :param loc: the location to place the mark
        :return: GAMEOVER | PLACE_SUCCESS | PLACE_FAIL
        '''

        if loc in self.location and (self.location[loc] != self.PLAYERX or self.location[loc] == self.PLAYERO):
            board_loc = self.location[loc]
            self.board[board_loc[0]][board_loc[1]] = self.current_player
            self.remaining_moves -= 1

            status = self.check_victory(self.remaining_moves, self.board)
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

            self.current_player = self.switch_player(self.current_player)
            return self.PLACE_SUCCESS
        else:
            print('Position is already taken or is invalid! ')
            print()
            return self.PLACE_FAIL

    def switch_player(self, player):
        if player == self.PLAYERX:
            return self.PLAYERO
        else:
            return self.PLAYERX

    def check_victory(self, remaining_moves, board):
        '''
        Checks whether the passed in board resulted in a victory or tie.
        Independent of current game state.

        :param remaining_moves: remaining moves left on the passed in board
        :param board: board for which victory will be checked
        :return: TIE | VICTORY | PLAY_ON
        '''

        if self.check_victory_row(board) or self.check_victory_column(board) or self.check_victory_diagonal(board):
            return self.VICTORY
        if remaining_moves == 0:
            return self.TIE
        return self.PLAY_ON

    def check_victory_row(self, board):
        for i in range(3):
            if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
                return True

        return False

    def check_victory_column(self, board):
        for i in range(3):
            if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
                return True

        return False

    def check_victory_diagonal(self, board):
        if (board[0][0] == board[1][1] and board[0][0] == board[2][2]) or \
                (board[0][2] == board[1][1] and board[0][2] == board[2][0]):
            return True

        return False




    def alpha_beta(self, board, current_player, alpha, beta):
        possible_moves = self.possible_moves(board)

        status = self.check_victory(len(possible_moves), board)
        if status == self.VICTORY:
            if current_player == self.PLAYERO:
                return -10;
            else:
                return 10;
        elif status == self.TIE:
            return 0;

        if current_player == self.PLAYERO:
            # print("PLAYER0 making a move")
            for move in possible_moves:
                new_board = copy.deepcopy(board)
                board_loc = self.location[move]
                new_board[board_loc[0]][board_loc[1]] = current_player
                # self.print_passed_board(new_board)
                # print()

                score = self.alpha_beta(new_board, self.switch_player(current_player), alpha, beta)
                # print("score: " + str(score))
                if score > alpha:
                    # print("alpha = score")
                    alpha = score
                if alpha >= beta:
                    # print("alpha >= beta")
                    return alpha;

            return alpha
        else:
            # print("PLAYERX making a move")
            for move in possible_moves:
                new_board = copy.deepcopy(board)
                board_loc = self.location[move]
                new_board[board_loc[0]][board_loc[1]] = current_player
                # self.print_passed_board(new_board)
                # print()

                score = self.alpha_beta(new_board, self.switch_player(current_player), alpha, beta)
                # print("score: " + str(score))
                if score < beta:
                    # print("beta = score")
                    beta = score
                if alpha >= beta:
                    # print("alpha >= beta")
                    return beta;

            return beta

    def possible_moves(self, board):
        ret = []
        for i in range(3):
            for j in range(3):
                if board[i][j] is not self.PLAYERX and board[i][j] is not self.PLAYERO:
                    ret.append(board[i][j])

        return ret

    def print_passed_board(self, board):
        '''
        Prints the passed in board.
        '''

        print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
        print("-----------")
        print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
        print("-----------")
        print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])


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

            inf = math.inf
            print("ALPHA_BETA")
            score = self.alpha_beta(self.board, self.current_player, -inf, inf)
            print(score)

            # self.place(score[1])
            # print()
            # self.print_board()
            # print()


if __name__ == "__main__":
    game = TicTacToe()
    game.start_game()
