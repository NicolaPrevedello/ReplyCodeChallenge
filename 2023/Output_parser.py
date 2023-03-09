
import csv
import random
from collections import defaultdict
import numpy as np
import pandas as pd


class SnakeInfo:
    def __init__(self, index, position):
        self.index = index
        self.position = position

class SnakePosition:

    def __init__(self, c, r):
        self.c = c
        self.r = r

     def __str__(self):
         return "Snake position: {},{}".format(c,r)


class SnakeDirection:
    def __init__(self, direction, snake_position):
        self.direction = direction


class RelevanceMatrix:
    def __init__(self, c, r):
        self.c = c
        self.r = r
        self.matrix = np.zeros(r, c)

    def compute_next_position(self, direction, snakePos):
        if self.matrix[snakePos.r, snakePos.c] == '*':

n_wormhole = 5

def scegli_wormhole_random():
    return random.randint(0, n_wormhole-1)

def next_position_without_wormhole(pos, direction, c, r):
    if direction == 'U':  # Up
        if pos.r - 1 < 0:
            pos.r = r - 1
        else:
            pos.r -= 1
    elif direction == 'D':  # down
        if pos.r + 1 == r:
            pos.r = 0
        else:
            pos.r += 1
    elif direction == 'R':  # right
        if pos.c + 1 == c:
            pos.c = 0
        else:
            pos.c += 1
    elif direction == 'L':  # left
        if pos.c - 1 < 0:
            pos.c = c - 1
        else:
            pos.c -= 1
    return pos

def get_neighbor_wormhole_position(pos, c, r):
    new_pos_up = SnakePosition(pos.c, pos.r)
    if new_pos_up.r - 1 < 0:  # Up
        new_pos_up.r = r - 1
    else:
        new_pos_up.r -= 1

    new_pos_down = SnakePosition(pos.c, pos.r)
    if new_pos_down.r + 1 == r:
        new_pos_down.r = 0
    else:
        new_pos_down.r += 1

    new_pos_right = SnakePosition(pos.c, pos.r)
    if new_pos_right.c + 1 == c:
        new_pos_right.c = 0
    else:
        new_pos_right.c += 1

    new_pos_left = SnakePosition(pos.c, pos.r)
    if new_pos_left.c - 1 < 0:
        new_pos_left.c = c - 1
    else:
        new_pos_left.c -= 1

    return [new_pos_left, new_pos_right, new_pos_down, new_pos_up]



wormhole_positions = {}

def next_position_with_wormhole(pos, direction, c, r):
    pos = next_position_with_wormhole(pos, direction, c, r)
    if pos in wormhole_positions:

        wormhole_position = scegli_wormhole_random()

    return pos




def parse_output_file(filename, c, r):
    with open(filename) as f:
        reader = csv.reader(f, delimiter=' ')
        snakes_number = len(list(reader))
        for row in range(snakes_number):
            splitted_line = list(reader)[row]  # get iesima riga
            current_pos = SnakePosition(splitted_line[0], splitted_line[1])
            current_snake =  SnakeInfo(row, current_pos)
            i_step = 2
            directions = []
            wormhole_position = []
            snakes = []
            while i_step < len(splitted_line):
                if splitted_line[i_step] in ('U', 'D', 'L', 'R'):
                    next_position_with_wormhole(current_pos, splitted_line[i_step], c, r):
                    directions.append(splitted_line[i_step])
                else:
                    snakes.append(current_snake)

                    new_position = SnakePosition(splitted_line[i_step], splitted_line[i_step+1])
                    wormhole_position.append(new_position)



            if len(splitted_line) > 3:
                next_position = SnakePosition(splitted_line[3], splitted_line[4])
