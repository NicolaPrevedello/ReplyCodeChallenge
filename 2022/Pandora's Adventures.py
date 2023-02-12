import numpy as np
from InputParser import parseInput
from Utility import *


startMana,maxMana,totalRounds,monsterToFace,monsterDesc,rewardList = parseInput("./2022/00-example.txt")



#Inizio algoritmo soluzione ottima
mana = startMana

for i in range(totalRounds):

    #Trovo i mostri che posso affrontare
    availableMonster = []
    for j in range(monsterDesc.shape[0]):
        if(monsterDesc[j][0] < mana):
            availableMonster.append(j)

    scores = scoreFunction(availableMonster, monsterDesc, rewardList, totalRounds-i)
    print("Round {} Monsters {} scores: {}".format(i, availableMonster, scores))










