//
// Created by King on 2021.4.26.
//

#include "Board.h"
#include "Pieces.h"
#include "States.h"
#include "shape.h"
#include <fstream>

using namespace std;

struct position solution[7];

Pieces pieces[7];

Board board;

bool done[7] = {false};

int getNextPieces_Type(void);
int getNextPieces(int pieceType);

void given_solution() {
    ofstream out("solution.txt");
    for (int i = 0; i < 7; i++) {
        out << i << " " << solution[i].x << " " << solution[i].y << " " << solution[i].rotate_number;
    }
}

void bfs() {
    int PieceID = getNextPieces(getNextPieces_Type());
    for (int i = 0; i < BoardLength; i++)
        for (int j = 0; j < BoardWidth; j++) {
            int rotate = board.put_pieces(pieces[PieceID], i, j);
            if (rotate != -1 && rotate != -2) {
                bool mark = true;
                for (int k = 0; k < 7; k++) {
                    if (!done[k]) {
                        mark = false;
                        break;
                    }
                }
                if (mark) {
                    given_solution();
                    board.remove_pieces(pieces[PieceID], solution[PieceID]);
                    board.remove_pieces(pieces[6 - PieceID], solution[6 - PieceID]);
                }
                solution[PieceID] = {i, j, rotate};
                done[PieceID] = true;
                for (int i = 0; i < 7; i++) {
                    if (!done[i]) {
                        bfs();
                        board.remove_pieces(pieces[PieceID], solution[PieceID]);
                        done[PieceID] = false;
                    }
                }
            } else {
                continue;
            }
        }

};


int getNextPieces_Type(void) {
    if ((!done[0]) || (!done[1])) return PieceType::LARGE_TRIANGLE;
    else if ((!done[2])) return PieceType::MID_TRIANGLE;
    else if ((!done[3]) || (!done[4])) return PieceType::SMALL_TRIANGLE;
    else if ((!done[5])) return PieceType::SQUARE;
    else return PieceType::PARALLELOGRAM;
}

int getNextPieces(int pieceType) {
    switch (pieceType) {
        case PieceType::LARGE_TRIANGLE:
            return done[0] ? 1 : 0;
        case PieceType::MID_TRIANGLE:
            return 2;
        case PieceType::SMALL_TRIANGLE:
            return done[3] ? 4 : 3;
        case PieceType::SQUARE:
            return 5;
        case PieceType::PARALLELOGRAM:
            return 6;
    }
}

Pieces init_Lar_tran() {
    shape s;
    Pieces p;
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 2; j++) {
            p.rotate_1[i][j] = s.piece1[i][j];
            p.rotate_3[i][j] = s.piece1_270[i][j];
        }
    p.sizeA.length = 4;
    p.sizeD.length = 2;
    p.sizeA.width = 2;
    p.sizeD.width = 4;
    p.sizeB.width = 2;
    p.sizeB.length = 4;
    p.sizeC.width = 4;
    p.sizeC.length = 2;

    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 4; j++) {
            p.rotate_2[i][j] = s.piece1_90[i][j];
            p.rotate_4[i][j] = s.piece1_180[i][j];
        }
    return p;
}


Pieces init_Mid_tran() {
    shape s;
    Pieces p;
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++) {
            p.rotate_1[i][j] = s.piece3[i][j];
            p.rotate_4[i][j] = s.piece3_270[i][j];
        }
    p.sizeA.length = 2;
    p.sizeD.length = 2;
    p.sizeA.width = 2;
    p.sizeD.width = 2;
    p.sizeB.width = 2;
    p.sizeB.length = 2;
    p.sizeC.width = 2;
    p.sizeC.length = 2;

    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++) {
            p.rotate_2[i][j] = s.piece3_90[i][j];
            p.rotate_3[i][j] = s.piece3_180[i][j];
        }
    return p;
}

Pieces init_Sma_tran() {
    shape s;
    Pieces p;
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 1; j++) {
            p.rotate_1[i][j] = s.piece4[i][j];
            p.rotate_3[i][j] = s.piece4_270[i][j];
        }
    p.sizeA = {2, 1};
    p.sizeC = {2, 1};
    p.sizeB = {1, 2};
    p.sizeD = {1, 2};

    for (int i = 0; i < 1; i++)
        for (int j = 0; j < 2; j++) {
            p.rotate_2[i][j] = s.piece4_90[i][j];
            p.rotate_4[i][j] = s.piece4_180[i][j];
        }
    return p;
}

Pieces init_squ() {
    shape s;
    Pieces p;
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++) {
            p.rotate_1[i][j] = s.piece6[i][j];
        }
    p.sizeA = {2, 2};
    return p;
}

Pieces init_par() {
    shape s;
    Pieces p;
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 1; j++) {
            p.rotate_1[i][j] = s.piece7[i][j];
        }
    for (int i = 0; i < 1; i++)
        for (int j = 0; j < 3; j++) {
            p.rotate_1[i][j] = s.piece7[i][j];
        }
    p.sizeA = {3, 1};
    p.sizeB = {1, 3};
}

Board getBoard(int bid) {
    shape s;
    Board b;
    switch (bid) {
        case 0:
            for (int i = 0; i < 8; i++)
                for (int j = 0; j < 6; j++)
                    b.board[i][j].type = s.large_tri1[i][j];
            break;
        case 1:
            for (int i = 0; i < 8; i++)
                for (int j = 0; j < 6; j++)
                    b.board[i][j].type = s.large_squ2[i][j];
            break;
        case 2:
            for (int i = 0; i < 8; i++)
                for (int j = 0; j < 6; j++)
                    b.board[i][j].type = s.large_par3[i][j];
            break;
        case 3:
            for (int i = 0; i < 8; i++)
                for (int j = 0; j < 6; j++)
                    b.board[i][j].type = s.large_par4[i][j];
            break;
        case 4:
            for (int i = 0; i < 8; i++)
                for (int j = 0; j < 6; j++)
                    b.board[i][j].type = s.large_tra5[i][j];
            break;
        case 5:
            for (int i = 0; i < 8; i++)
                for (int j = 0; j < 6; j++)
                    b.board[i][j].type = s.large_ritra6[i][j];
            break;
        case 6:
            for (int i = 0; i < 8; i++)
                for (int j = 0; j < 6; j++)
                    b.board[i][j].type = s.large_ritra7_oppsite[i][j];
            break;
        case 7:
            for (int i = 0; i < 8; i++)
                for (int j = 0; j < 6; j++)
                    b.board[i][j].type = s.large_irr8[i][j];
            break;
        case 8:
            for (int i = 0; i < 8; i++)
                for (int j = 0; j < 6; j++)
                    b.board[i][j].type = s.large_irr9[i][j];
            break;
        case 9:
            for (int i = 0; i < 8; i++)
                for (int j = 0; j < 6; j++)
                    b.board[i][j].type = s.large_pol10[i][j];
            break;
        case 10:
            for (int i = 0; i < 8; i++)
                for (int j = 0; j < 6; j++)
                    b.board[i][j].type = s.large_pol11[i][j];
            break;
        case 11:
            for (int i = 0; i < 8; i++)
                for (int j = 0; j < 6; j++)
                    b.board[i][j].type = s.large_irr12[i][j];
            break;
        case 12:
            for (int i = 0; i < 8; i++)
                for (int j = 0; j < 6; j++)
                    b.board[i][j].type = s.large_pol13[i][j];
            break;
    }
}

void init(int boardID) {
    board = getBoard(boardID);
    for (int i = 0; i < 7; i++) {
        switch (i) {
            case 0:
            case 1:
                pieces[i] = init_Lar_tran();
                pieces[i].pieceType = PieceType::LARGE_TRIANGLE;
                pieces[i].init();
                break;
            case 2:
                pieces[i] = init_Mid_tran();
                pieces[i].pieceType = PieceType::MID_TRIANGLE;
                pieces[i].init();
                break;
            case 3:
            case 4:
                pieces[i] = init_Sma_tran();
                pieces[i].pieceType = PieceType::SMALL_TRIANGLE;
                pieces[i].init();
                break;
            case 5:
                pieces[i] = init_squ();
                pieces[i].pieceType = PieceType::SQUARE;
                pieces[i].init();
                break;
            case 6:
                pieces[i] = init_par();
                pieces[i].pieceType = PieceType::PARALLELOGRAM;
                pieces[i].init();
                break;
        }
    }
}


int main(int argc, char **argv) {
    int bid = atoi(argv[1]);
    init(bid);
    bfs();
    return 0;
}