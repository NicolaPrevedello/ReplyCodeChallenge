import numpy as np
import random
from InputParser import parseInput
from Utility import *

dataSet0 = "00-example"
dataSet1 = "01-the-cloud-abyss"
dataSet2 = "02-iot-island-of-terror"
dataSet3 = "03-etheryum"
dataSet4 = "04-the-desert-of-autonomous-machines"
dataSet5 = "05-androids-armageddon"

dataSetInTesting = dataSet0

startStamina,maxStamina,totalRounds,monsterToFace,monsterDesc,rewardList = parseInput("./2022/" + dataSetInTesting + ".txt")


#Inizio algoritmo
bestSolution = 0.0
iteration = 0
numIterazioni = 1000


while iteration<numIterazioni:

    stamina = np.full(totalRounds,startStamina)
    actualSolution = np.full(totalRounds, -1)

    for i in range(totalRounds):

        #Trovo i mostri che posso affrontare
        availableMonster = []
        for j in range(monsterDesc.shape[0]):
            if(monsterDesc[j][0] <= stamina[i]):
                availableMonster.append(j)
        
        availableMonster = removeAlreadyDefeated(availableMonster, actualSolution)

        if(len(availableMonster)>0):
            scores = rankFunction(availableMonster, monsterDesc, rewardList, totalRounds-i)
            #print("Iteration {} Round {} Monsters {} scores: {}".format(iteration, i, availableMonster, scores))


            #Scelta basata SOLO SULLA MASSIMA SOMMA DELLE REWARDS
            #choice = availableMonster[np.argmax(scores)]

            #Scelta PROBABILISTICA BASATA SULLA MASSIMA SOMMA DELLE REWARDS
            total = np.sum(scores)
            if total != 0:
                probabilities = [v/total for v in scores]
                chosenRank = random.choices(scores, weights=probabilities)[0]
                choice = availableMonster[scores.tolist().index(chosenRank)]
            else:
                probabilities = np.ones(len(scores))/len(scores)
                chosenRank = random.choices(scores, weights=probabilities)[0]
                choice = availableMonster[scores.tolist().index(chosenRank)]

            
            actualSolution[i] = choice
            
            #Rimuovo la stamina consumata e aggiungo quella guadagnata
            stamina[i+1:] = stamina[i+1:] - monsterDesc[choice][0]
            stamina[i+monsterDesc[choice][1]:] = stamina[i+monsterDesc[choice][1]:] + monsterDesc[choice][2]

            stamina = checkStamina(stamina, maxStamina)

        else:
            actualSolution[i] = -1

    solutionScore = solutionFinalScore(actualSolution, rewardList)
    print("ITERAZIONE {} PUNTEGGIO SOLUZIONE: {}".format(iteration, solutionScore))

    if(solutionScore>bestSolution):
        bestSolution = solutionScore
        saveSolution(actualSolution, iteration, solutionScore, "./2022/Solutions/" + dataSetInTesting + "/")
    
    iteration += 1

print("BEST SOLUTION: ", bestSolution)










