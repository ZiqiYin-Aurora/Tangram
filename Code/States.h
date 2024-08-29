//
// Created by King on 2021.4.25.
//

#ifndef PROJECT_STATES_H
#define PROJECT_STATES_H

#define EMPTY 0
#define LEFT_TOP 1
#define RIGHT_TOP 2
#define LEFT_DOWN 3
#define RIGHT_DOWN 4
#define FULL 5

enum PieceType{LARGE_TRIANGLE, MID_TRIANGLE, SMALL_TRIANGLE, SQUARE, PARALLELOGRAM};

struct position{
    int x;
    int y;
    int rotate_number;
};


#endif //PROJECT_STATES_H
