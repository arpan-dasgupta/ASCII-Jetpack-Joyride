class Board:
    def __init__(self):
        # init empty board
        self.size = 8
        self.board = [['-' for j in range(self.size)] for i in range(self.size)]
        self.numOccupied = 0
        self.counts = {}
        self.isGameOver = False


    def print_board(self):
        print("\n==============================================")
        for i in range(self.size):
            for j in range(self.size):
                print(self.board[i][j], end=" ")
            print("")
        print("==============================================\n")


    def gameOver(self):
        #returns the winning symbol or -1 in case of a draw or -2 in case of game not over
        if self.numOccupied == self.size ** 2:
            self.isGameOver = True
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j] in self.counts:
                        self.counts[self.board[i][j]] += 1
                    else:
                        self.counts[self.board[i][j]] = 1

            #get list of playing symbols
            symbols = list(self.counts.keys())

            #total domination
            if len(symbols) == 1:
                return symbols[0]
            #check winner or draw
            else:
                if self.counts[symbols[0]] > self.counts[symbols[1]]:
                    return symbols[0]
                elif self.counts[symbols[0]] < self.counts[symbols[1]]:
                    return symbols[1]
                else:
                    return -1


    def check_valid(self, i, j):
        if self.board[i][j] == '-':
            return True
        return False


    def update(self, i, j, c):
        # put in place
        self.board[i][j] = c
        self.numOccupied += 1

        #update vertically up
        k = i - 1
        willFlip = False
        while k >= 0 and self.board[k][j] != '-':
            if self.board[k][j] == c:
                willFlip = True
                break
            k -= 1
        if k != -1 and willFlip:
            for q in range(i-1, k, -1):
                self.board[q][j] = c

        #update vertically down
        k = i + 1
        willFlip = False
        while k < self.size and self.board[k][j] != '-':
            if self.board[k][j] == c:
                willFlip = True
                break
            k += 1
        if k != self.size and willFlip:
            for q in range(i+1, k):
                self.board[q][j] = c

        #update horizontally left
        k = j - 1
        willFlip = False
        while k >= 0 and self.board[i][k] != '-':
            if self.board[i][k] == c:
                willFlip = True
                break
            k -= 1
        if k != -1 and willFlip:
            for q in range(j-1, k, -1):
                self.board[i][q] = c

        #update horizontally right
        k = j + 1
        willFlip = False
        while k < self.size and self.board[i][k] != '-':
            if self.board[i][k] == c:
                willFlip = True
                break
            k += 1
        if k != self.size and willFlip:
            for q in range(j+1, k):
                self.board[i][q] = c

        # update diagonally top-left
        k = i - 1
        l = j - 1
        willFlip = False
        while k >= 0 and l >= 0 and self.board[k][l] != '-':
            if self.board[k][l] == c:
                willFlip = True
                break
            k -= 1
            l -= 1
        if k != -1 and l != -1 and willFlip:
            w = j - 1
            for q in range(i-1, k, -1):
                self.board[q][w] = c
                w -= 1

        # update diagonally top-right
        k = i - 1
        l = j + 1
        willFlip = False
        while k >= 0 and l < self.size and self.board[k][l] != '-':
            if self.board[k][l] == c:
                willFlip = True
                break
            k -= 1
            l += 1
        if k != -1 and l != self.size and willFlip:
            w = j + 1
            for q in range(i-1, k, -1):
                self.board[q][w] = c
                w += 1

        # update diagonally bottom-left
        k = i + 1
        l = j - 1
        willFlip = False
        while k < self.size and l >= 0 and self.board[k][l] != '-':
            if self.board[k][l] == c:
                willFlip = True
                break
            k += 1
            l -= 1
        if k != self.size and l != -1 and willFlip:
            w = j - 1
            for q in range(i+1, k):
                self.board[q][w] = c
                w -= 1

        # update diagonally bottom-right
        k = i + 1
        l = j + 1
        willFlip = False
        while k < self.size and l < self.size and self.board[k][l] != '-':
            if self.board[k][l] == c:
                willFlip = True
                break
            k += 1
            l += 1
        if k != self.size and l != self.size and willFlip:
            w = j + 1
            for q in range(i+1, k):
                self.board[q][w] = c
                w += 1
