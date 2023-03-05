import numpy as np
import random
from InputParser import parseInput
from Utility import *

#FILE DEDICATO AI TEST DELLE FUNZIONI 

dataSet0 = "00-example"
dataSet1 = "01-the-cloud-abyss"
dataSet2 = "02-iot-island-of-terror"
dataSet3 = "03-etheryum"
dataSet4 = "04-the-desert-of-autonomous-machines"
dataSet5 = "05-androids-armageddon"

dataSetInTesting = dataSet0

#Input Parser in base al dataSet che voglio analizzare
startStamina,maxStamina,totalRounds,monsterToFace,monsterDesc,rewardList = parseInput("./2022/" + dataSetInTesting + ".txt")


# stamina = np.full(totalRounds, 5)
# print("STAMINA ATTUALE", stamina)
# stamina[3:] = stamina[3:] + np.full(totalRounds - 3, 20)
# print("STAMINA AGGIORNATA", stamina)
# stamina = checkStamina(stamina, maxStamina)
# print("STAMINA FINALE", stamina)


print_in_a_frame("WELCOME IN PANDORA`S ADVENTURES")
