//
// Created by King on 2021.4.25.
//

#ifndef PROJECT_PIECES_H
#define PROJECT_PIECES_H

#include <vector>

using namespace std;

struct pieceSize {
    int length;
    int width;
};

class Pieces {
public:

    int pieceType;

    int rotatePossibility;

    vector<vector<int>> rotate_1;
    vector<vector<int>> rotate_2;
    vector<vector<int>> rotate_3;
    vector<vector<int>> rotate_4;

    struct pieceSize sizeA;
    struct pieceSize sizeB;
    struct pieceSize sizeC;
    struct pieceSize sizeD;

    void init();
    int setRotatePossibility(void);
};


#endif //PROJECT_PIECES_H
