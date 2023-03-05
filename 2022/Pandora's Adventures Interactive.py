import numpy as np
import random
from InputParser import parseInput
from Utility import *


'''
PER POTER ESEGUIRE QUESTO FILE È NECESSARIO:
    -SCEGLIERE IL DATASET DA ANALIZZARE
    -SEGUIRE LE INDICAZIONI DATE A TERMINALE
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


#Setting dei parametri locali (propri di ogni iterazione)
stamina = np.full(totalRounds,startStamina)
actualSolution = np.full(totalRounds, -1)
facedMonster = 0

print_in_a_frame("WELCOME IN PANDORA`S ADVENTURES")

#Simulo ciascun round di ogni iterazione
for i in range(totalRounds):

    print("ROUND {}:".format(i))
    print("STAMINA {}".format(stamina[i]))

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
            

            total = np.sum(scores)
            probabilities = []
            if total != 0:
                probabilities = [v/total for v in scores]
            else:
                probabilities = np.ones(len(scores))/len(scores)
                
            print("In questo round sono disponibili i seguenti mostri:")
            for k in range(len(availableMonster)):
                print("Mostro #{} Costo stamina: {} Somma delle reward restanti {} Probabilità di scelta: {} Stamina gain: {} Delay: {}".format(availableMonster[k],monsterDesc[availableMonster[k]][0],scores[k],probabilities[k], monsterDesc[availableMonster[k]][2], monsterDesc[availableMonster[k]][1]))

            choice = int(input("Scegli un mostro: "))

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

print("SOLUTION: ", solutionScore)

print_in_a_frame("END OF THE ADVENTURE")
