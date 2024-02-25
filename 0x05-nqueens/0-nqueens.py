#!/usr/bin/python3
"""Module to solve N queens challenge"""
import sys


def nqueens(N: int):
    """Method solves n queens on nxn chessboard question"""
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    def check_queens(board, row, col):
        """checks if queen in same col or diagonal"""
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == row - i:
                return False

        return True

    def solve(board, row):
        """solves n queens question challenge"""
        if row == N:
            print_board(board)
            return

        for col in range(N):
            if check_queens(board, row, col):
                board[row] = col
                solve(board, row + 1)

    def print_board(board):
        """prints board"""
        print([[i, board[i]] for i in range(N)])

    board = [-1] * N
    solve(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
