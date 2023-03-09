import csv
import numpy as np


#Input parser

def parseInput(fileName):

    with open(fileName) as f:
        reader = csv.reader(f, delimiter=' ')

        lines = list(reader)

        cnt = 0
        for row in lines:
            row = list(filter(bool, row))

            if cnt == 0:
                cols = int(row[0])
                rows = int(row[1])
                snakes = int(row[2])  
                snakesLentgths = np.full(snakes, -1)
                ground = np.zeros((rows, cols), int)

            if cnt == 1:
                for i in range(snakes):
                    snakesLentgths[i] = row[i]

            if cnt > 1:
                for j in range(cols):
                    if(row[j] == "*"):
                        ground[cnt-2][j] = -5
                    else:
                        ground[cnt-2][j] = row[j]

            cnt += 1 

    return rows,cols,snakesLentgths,ground