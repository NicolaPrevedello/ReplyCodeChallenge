import numpy as np
import random
from InputParser import parseInput
from Utility import *
import csv

dataSet0 = "00-example"
dataSet1 = "01-chilling-cat"
dataSet2 = "02-swarming-ant"
dataSet3 = "03-input-anti-greedy"
dataSet4 = "04-input-low-points"
dataSet5 = "05-input-opposite-points-holes"

datasets = [dataSet0, dataSet1, dataSet2, dataSet3, dataSet4, dataSet5]

#,

for i in range(6):
    dataSetInTesting = datasets[i]

    #Input Parser in base al dataSet che voglio analizzare
    rows,cols,snakes,snakesLentgths,ground = parseInput("./2023/" + dataSetInTesting + ".txt")
    print("NUMERO DI RIGHE: ", rows)
    print("NUMERO DI COLONNE: ", cols)
    print("LUNGHEZZA DEGLI SNAKES: ", snakesLentgths)
    print("GROUND: \n", ground)


    with open("./SOLUZIONE{}.txt".format(i), "w") as file:
        # scrivi ogni numero seguito dal carattere di nuova linea (\n)
            
                    

        for j in range(snakes):
            solution = ""
            max_position = np.where(ground == np.amax(ground))
            lastPosition = np.full(2, -1)
            #print("SNAKE:", snakesLentgths[j])
            for i in range(snakesLentgths[j]):
                if(i == 0 ):
                    lastPosition[0] = max_position[0][0]
                    lastPosition[1] = max_position[1][0]
                    solution = str(lastPosition[1]) + " " + str(lastPosition[0])
                    #print(ground[lastPosition[0]][lastPosition[1]])
                    ground[lastPosition[0]][lastPosition[1]] = -1000000
                else:
                    if (lastPosition[0]+1>=ground.shape[0]):
                        lastPosition[0] = 0
                        continue
                    if (lastPosition[1]+1>=ground.shape[1]):
                        lastPosition[1] = 0
                        continue
                    if (lastPosition[0]-1<0):
                        lastPosition[0] = ground.shape[0]-1
                        continue
                    if (lastPosition[1]-1<0):
                        lastPosition[1] = ground.shape[1]-1
                        continue
                    
                    values = [ground[lastPosition[0]+1][lastPosition[1]], ground[lastPosition[0]-1][lastPosition[1]], ground[lastPosition[0]][lastPosition[1]+1], ground[lastPosition[0]][lastPosition[1]-1]]
                    maxValue = np.max(values)
                    if(maxValue == ground[lastPosition[0]+1][lastPosition[1]]):
                        solution +=  " " + "D"
                        lastPosition[0] = lastPosition[0] + 1
                        lastPosition[1] = lastPosition[1]
                    elif(maxValue == ground[lastPosition[0]-1][lastPosition[1]]):
                        solution +=  " " + "U"
                        lastPosition[0] = lastPosition[0] - 1
                        lastPosition[1] = lastPosition[1]
                    elif(maxValue == ground[lastPosition[0]][lastPosition[1]+1]):
                        solution +=  " " + "R"
                        lastPosition[0] = lastPosition[0]
                        lastPosition[1] = lastPosition[1] + 1
                    elif(maxValue == ground[lastPosition[0]][lastPosition[1]-1]):
                        solution +=  " " + "L"
                        lastPosition[0] = lastPosition[0]
                        lastPosition[1] = lastPosition[1] -1
                    #print(ground[lastPosition[0]][lastPosition[1]])
                    ground[lastPosition[0]][lastPosition[1]] = -1000000
            
            file.write(solution + "\n")
        print("CIAO")


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
                        ground[cnt-2][j] = -1000000
                    else:
                        ground[cnt-2][j] = row[j]

            cnt += 1 

    return rows,cols,snakes,snakesLentgths,ground