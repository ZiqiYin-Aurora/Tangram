//
// Created by King on 2021.4.25.
//

#include "Board.h"
#include "States.h"


bool Board::gameCheck() {
    for (int i = 0; i < BoardLength; i++)
        for (int j = 0; j < BoardWidth; j++) {
            if (this->board[i][j].type != FULL)
                return false;
        }
    return true;
}


int Board::h_n() {
    int hn = 0;
    for (int i = 0; i < BoardLength; i++)
        for (int j = 0; j < BoardWidth; j++) {
            if (this->board[i][j].type == FULL)
                hn++;
        }
    return hn;
}

void Board::init() {
    for (int i = 0; i < BoardLength; i++)
        for (int j = 0; j < BoardWidth; j++) {
            if (this->board[i][j].type == FULL)
                this->board[i][j].locked = true;
            else
                this->board[i][j].locked = false;
        }
}


int Board::put_pieces(Pieces pieces, int i, int j) {
    if (pieces.rotatePossibility == 1) {

        if (Match(pieces.rotate_1, pieces.sizeA, i, j) == 1) {
            lock(pieces.rotate_1, pieces.sizeA, i, j);
            return 0;
        } else
            return -1;
    } else if (pieces.rotatePossibility == 2) {

        if (Match(pieces.rotate_1, pieces.sizeA, i, j) == 1) {
            lock(pieces.rotate_1, pieces.sizeA, i, j);
            return 0;
        } else if (Match(pieces.rotate_2, pieces.sizeB, i, j) == 1) {
            lock(pieces.rotate_2, pieces.sizeB, i, j);
            return 1;
        } else return -1;
    } else if (pieces.rotatePossibility == 4) {
        if (Match(pieces.rotate_1, pieces.sizeA, i, j) == 1) {
            lock(pieces.rotate_1, pieces.sizeA, i, j);
            return 0;
        } else if (Match(pieces.rotate_2, pieces.sizeB, i, j) == 1) {
            lock(pieces.rotate_2, pieces.sizeB, i, j);
            return 1;
        } else if (Match(pieces.rotate_3, pieces.sizeC, i, j) == 1) {
            lock(pieces.rotate_3, pieces.sizeC, i, j);
            return 2;
        } else if (Match(pieces.rotate_4, pieces.sizeD, i, j) == 1) {
            lock(pieces.rotate_4, pieces.sizeD, i, j);
            return 3;
        } else return -1;
    } else return -2;
}

int Board::Match(vector<vector<int>> format, struct pieceSize size, int x, int y) {
    for (int i = 0; i < size.length && (i + x) < BoardLength; i++) {
        for (int j = 0; j < size.width && (j + y) < BoardWidth; i++) {
            if (format[i][j] + board[i + x][j + y].type == FULL || board[i + x][j + y].type == EMPTY) continue;
            else return 0;
        }
    }
    return 1;
}

void Board::lock(vector<vector<int>> format, struct pieceSize size, int x, int y) {
    for (int i = 0; i < size.length && (i + x) < BoardLength; i++) {
        for (int j = 0; j < size.width && (j + y) < BoardWidth; i++) {
            board[i + x][j + y].type += format[i][j];
        }
    }
}

void Board::remove_pieces(Pieces pieces, struct position position) {
    switch (position.rotate_number) {
        case 1:
            unlock(pieces.rotate_1, pieces.sizeA, position.x, position.y);
            return;
        case 2:
            unlock(pieces.rotate_2, pieces.sizeB, position.x, position.y);
            return;
        case 3:
            unlock(pieces.rotate_3, pieces.sizeC, position.x, position.y);
            return;
        case 4:
            unlock(pieces.rotate_4, pieces.sizeD, position.x, position.y);
            return;
    }
}

void Board::unlock(vector<vector<int>> v, struct pieceSize size, int x, int y) {
    for (int i = 0; i < size.length && (i + x) < BoardLength; i++) {
        for (int j = 0; j < size.width && (j + y) < BoardWidth; i++) {
            board[i + x][j + y].type -= v[i][j];
        }
    }
}