import numpy as np
import random
from InputParser import parseInput
from Utility import *


'''
PER POTER ESEGUIRE QUESTO FILE È NECESSARIO:
    -SCEGLIERE IL DATASET DA ANALIZZARE
    -IMPOSTARE IL NUMERO DI ITERAZIONI CHE SI DESIDERA ESEGUIRE
    -UNA VOLTA FINITO LE SOLUZIONI TROVATE VERRANNO SALVATE NEL PERCORSO: ./2022/Solutions/$dataSetInTesting/soluzioneMigliore.txt
'''

dataSet0 = "00-example"
dataSet1 = "01-the-cloud-abyss"
dataSet2 = "02-iot-island-of-terror"
dataSet3 = "03-etheryum"
dataSet4 = "04-the-desert-of-autonomous-machines"
dataSet5 = "05-androids-armageddon"

dataSetInTesting = dataSet0

#Input Parser in base al dataSet che voglio analizzare
startStamina,maxStamina,totalRounds,monsterToFace,monsterDesc,rewardList = parseInput("./2022/" + dataSetInTesting + ".txt")


#Setting dei parametri globali (comuni per ogni iterazione)
bestSolution = 0.0
currentIteration = 0
numIterazioni = 1000


while currentIteration<numIterazioni:

    #Setting dei parametri locali (propri di ogni iterazione)
    stamina = np.full(totalRounds,startStamina)
    actualSolution = np.full(totalRounds, -1)
    facedMonster = 0

    #Simulo ciascun round di ogni iterazione
    for i in range(totalRounds):

        if facedMonster <= monsterToFace:
            #Trovo i mostri che posso affrontare
            availableMonster = []
            for j in range(monsterDesc.shape[0]):
                if(monsterDesc[j][0] <= stamina[i]):
                    availableMonster.append(j)
            
            availableMonster = removeAlreadyDefeated(availableMonster, actualSolution)

            if(len(availableMonster)>0):
                #Calcolo la somma delle reward della lista degli availableMonster dal turno attuale fino alla fine
                scores = rankFunction(availableMonster, rewardList, totalRounds-i)
                #print("Iteration {} Round {} Monsters {} scores: {}".format(iteration, i, availableMonster, scores))

                #DUE POSSIBILI ALTERNATIVE PER EFFETTUARE LA SCELTA DEL MOSTRO DA AFFRONTARE

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

                #Registro la scelta nella soluzione attuale
                actualSolution[i] = choice
                
                #Rimuovo la stamina consumata e aggiungo quella guadagnata
                stamina[i+1:] = stamina[i+1:] - monsterDesc[choice][0]
                stamina[i+monsterDesc[choice][1]:] = stamina[i+monsterDesc[choice][1]:] + monsterDesc[choice][2]

                stamina = checkStamina(stamina, maxStamina)
                facedMonster += 1

            else:
                actualSolution[i] = -1

    #Calcolo il punteggio della soluzione attuale
    solutionScore = solutionFinalScore(actualSolution, rewardList)
    print("ITERAZIONE {} PUNTEGGIO SOLUZIONE: {}".format(currentIteration, solutionScore))

    if(solutionScore>bestSolution):
        bestSolution = solutionScore
        #Viene salvata la soluzione migliore nel percorso ./2022/Solutions/$dataSetInTesting/soluzioneMigliore.txt
        saveSolution(actualSolution, currentIteration, solutionScore, "./2022/Solutions/" + dataSetInTesting + "/")
    
    currentIteration += 1

print("BEST SOLUTION: ", bestSolution)










