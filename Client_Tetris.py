import numpy as np 
import pygame
import random

#                 0          1          2          3         4          5          6   
BLOCKS_IDX = ['BLOCK_I', 'BLOCK_O', 'BLOCK_Z', 'BLOCK_S', 'BLOCK_J', 'BLOCK_L', 'BLOCK_T']

BLOCKS = {
'BLOCK_I' : [
    [0,0,0,0,
    0,0,0,0,
    0,0,0,0,
    1,1,1,1],

    [0,0,1,0,
    0,0,1,0,
    0,0,1,0,
    0,0,1,0]],

'BLOCK_O' : [
    [0,0,0,0,
    0,0,0,0,
    0,1,1,0,
    0,1,1,0]
],

'BLOCK_Z' : [
    [0,0,0,0,
    0,0,1,0,
    0,1,1,0,
    0,1,0,0],

    [0,0,0,0,
    0,0,0,0,
    1,1,0,0,
    0,1,1,0]
],

'BLOCK_S' : [
    [0,0,0,0,
    0,1,0,0,
    0,1,1,0,
    0,0,1,0],

    [0,0,0,0,
    0,0,0,0,
    0,1,1,0,
    1,1,0,0]
],

'BLOCK_J' : [
    [0,0,0,0,
    0,0,1,0,
    0,0,1,0,
    0,1,1,0],

    [0,0,0,0,
    0,0,0,0,
    1,1,1,0,
    0,0,1,0],

    [0,0,0,0,
    0,1,1,0,
    0,1,0,0,
    0,1,0,0],

    [0,0,0,0,
    0,0,0,0,
    1,0,0,0,
    1,1,1,0]
],

'BLOCK_L' : [
    [0,0,0,0,
    0,1,0,0,
    0,1,0,0,
    0,1,1,0],
    
    [0,0,0,0,
    0,0,0,0,
    0,0,1,0,
    1,1,1,0],

    [0,0,0,0,
    0,1,1,0,
    0,0,1,0,
    0,0,1,0],

    [0,0,0,0,
    0,0,0,0,
    1,1,1,0,
    1,0,0,0]
],

'BLOCK_T' : [
    [0,0,0,0,
    0,0,0,0,
    1,1,1,0,
    0,1,0,0],

    [0,0,0,0,
    0,1,0,0,
    1,1,0,0,
    0,1,0,0],

    [0,0,0,0,
    0,0,0,0,
    0,1,0,0,
    1,1,1,0],

    [0,0,0,0,
    0,1,0,0,
    0,1,1,0,
    0,1,0,0]
]
}

class BLOCK : 
    def __init__(self, shape) : 
        self.shape = BLOCKS_IDX[shape] #string name of blocks
        self.len_types = len(BLOCKS[self.shape])
        self.type = 0
        self.locX = 0      #LEFT_TOP
        self.locY = 0

    def rotate(self, dir) : 
        if dir == 0 : #CCW
            self.type -= 1
        else :  #CW
            if self.type == len_types - 1 : 
                self.type = 0
            else : 
                self.type += 1

    def soft_drop(self) : 
        if(not check_collision(self.locX, self.locY+1)) : 
            self.locY -= 1

    def hard_drop(self) :
        while(not check_collision(self.locX, self.locY+1)) : 
            self.locY -= 1

    def moveX(self, dir) : 
        DX = [-1, 1]
        if(not check_collision(self.locX + DX[dir], self.locY)) : 
            self.locX += DX[dir]
        

    def check_rotate(self) : 
        pass

    def check_collision(self, tempX, tempY) : 
        pass
