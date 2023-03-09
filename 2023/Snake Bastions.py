import numpy as np
import random
from InputParser import parseInput
from Utility import *

dataSet0 = "00-example"
dataSet1 = "01-chilling-cat"
dataSet2 = "02-swarming-ant"
dataSet3 = "03-input-anti-greedy"
dataSet4 = "04-input-low-points"
dataSet5 = "05-input-opposite-points-holes"

dataSetInTesting = dataSet4

#Input Parser in base al dataSet che voglio analizzare
rows,cols,snakes,snakesLentgths,ground = parseInput("./2023/" + dataSetInTesting + ".txt")

print("NUMERO DI RIGHE: ", rows)
print("NUMERO DI COLONNE: ", cols)
print("LUNGHEZZA DEGLI SNAKES: ", snakesLentgths)
print("GROUND: \n", ground)


with open("./SOLUZIONE.txt", "w") as file:
    # scrivi ogni numero seguito dal carattere di nuova linea (\n)
        
                

    for j in range(snakes):
        solution = ""
        max_position = np.where(ground == np.amax(ground))
        lastPosition = np.full(2, -1)
        for i in range(snakesLentgths[j]):
            if(i == 0 ):
                lastPosition[0] = max_position[0][0]
                lastPosition[1] = max_position[1][0]
                solution = str(lastPosition[0]) + " " + str(lastPosition[1])
                ground[lastPosition[0]][lastPosition[1]] = -1
            else:
                if (lastPosition[0]+1>=ground.shape[0]):
                    lastPosition[0] = 0
                if (lastPosition[1]+1>=ground.shape[1]):
                    lastPosition[1] = 0
                
                values = [ground[lastPosition[0]+1][lastPosition[1]], ground[lastPosition[0]-1][lastPosition[1]], ground[lastPosition[0]][lastPosition[1]+1], ground[lastPosition[0]][lastPosition[1]-1]]
                maxValue = np.max(values)
                if(maxValue == ground[lastPosition[0]+1][lastPosition[1]]):
                    solution +=  " " + "R"
                    lastPosition[0] = lastPosition[0] + 1
                    lastPosition[1] = lastPosition[1]
                elif(maxValue == ground[lastPosition[0]-1][lastPosition[1]]):
                    solution +=  " " + "L"
                    lastPosition[0] = lastPosition[0] - 1
                    lastPosition[1] = lastPosition[1]
                elif(maxValue == ground[lastPosition[0]][lastPosition[1]+1]):
                    solution +=  " " + "D"
                    lastPosition[0] = lastPosition[0]
                    lastPosition[1] = lastPosition[1] + 1
                elif(maxValue == ground[lastPosition[0]][lastPosition[1]-1]):
                    solution +=  " " + "U"
                    lastPosition[0] = lastPosition[0]
                    lastPosition[1] = lastPosition[1] -1
                ground[lastPosition[0]][lastPosition[1]] = -1
        
        file.write(solution + "\n")
    print("CIAO")
