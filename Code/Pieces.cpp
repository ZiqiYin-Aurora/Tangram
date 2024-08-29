//
// Created by King on 2021.4.25.
//

#include "Pieces.h"
#include "States.h"

int Pieces::setRotatePossibility() {
    switch(this->pieceType){
        case PieceType::LARGE_TRIANGLE:
        case PieceType::MID_TRIANGLE:
        case PieceType::SMALL_TRIANGLE:
            return 4;
        case PieceType::SQUARE:
            return 1;
        case PieceType::PARALLELOGRAM:
            return 2;
    }
}

void Pieces::init() {
    this->rotatePossibility = this->setRotatePossibility();
    switch(this->rotatePossibility){
        case 4:
            this->sizeD.length = rotate_4.size();
            this->sizeD.width = rotate_4[0].size();
            this->sizeC.length = rotate_3.size();
            this->sizeC.width = rotate_3[0].size();
        case 2:
            this->sizeB.length = rotate_2.size();
            this->sizeB.width = rotate_2[0].size();
        case 1:
            this->sizeA.length = rotate_1.size();
            this->sizeA.width = rotate_1[0].size();
    }
}