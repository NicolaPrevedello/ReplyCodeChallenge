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

dataSetInTesting = dataSet0

#Input Parser in base al dataSet che voglio analizzare
rows,cols,snakesLentgths,ground = parseInput("./2023/" + dataSetInTesting + ".txt")

print("NUMERO DI RIGHE: ", rows)
print("NUMERO DI COLONNE: ", cols)
print("LUNGHEZZA DEGLI SNAKES: ", snakesLentgths)
print("GROUND: \n", ground)
