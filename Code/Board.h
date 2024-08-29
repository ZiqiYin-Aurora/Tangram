//
// Created by King on 2021.4.25.
//

#ifndef PROJECT_BOARD_H
#define PROJECT_BOARD_H

#include <vector>
#include <string>
#include "Pieces.h"

#define BoardLength 8
#define BoardWidth 6

struct node{
    int type;
    bool locked;
};

using namespace std;

class Board {
public:
    struct node board[8][6];
    bool gameCheck();
    int h_n();
    void init();
    int put_pieces(Pieces, int, int);
    int Match(vector<vector<int>>, struct pieceSize, int, int);
    void lock(vector<vector<int>>, struct pieceSize, int, int);
    void unlock(vector<vector<int>>, struct pieceSize, int, int);
    void remove_pieces(Pieces, struct position);
};


#endif //PROJECT_BOARD_H
