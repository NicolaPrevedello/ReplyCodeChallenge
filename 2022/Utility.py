import os
import numpy as np


def rankFunction(availableMonster, monsterDesc, rewardList, remainingRounds):

    rewardSumList = np.zeros(len(availableMonster))
    for i in range(len(availableMonster)):
        rewardSumList[i] = np.sum(rewardList[availableMonster[i]][:remainingRounds])

    #LA SOMMA DELLE REWARD NON BASTA A DEFINIRE LO SCORE... DA COMPLETARE

    

    return rewardSumList

#La monsterList che riceve deve avere un mostro per turno, se in un turno non si è preso nessun mostro va messo un -1
def solutionFinalScore(monsterList, rewardList):
    scorePerRound =  np.zeros(len(monsterList))
    for i in range(len(monsterList)):
        if(monsterList[i]>=0):
            scorePerRound[i:] += rewardList[monsterList[i]][:len(monsterList)-i]


    return np.sum(scorePerRound)


def saveSolution(solution, iteration, score, path):

    # apri il file in modalità scrittura (w)
    fileName = path+"Solution"+str(iteration)+"Score"+str(int(score))+".txt";

    directory = os.path.dirname(fileName)

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(fileName, "w") as file:
    # scrivi ogni numero seguito dal carattere di nuova linea (\n)
        for num in solution:
            if (num >= 0):
                file.write(str(num) + "\n")


def removeAlreadyDefeated(availableMonster, actualSolution):

    finalAvailableMonster = availableMonster.copy()

    for i in range(len(availableMonster)):
        if availableMonster[i] in actualSolution:
            finalAvailableMonster.remove(availableMonster[i])
    
    return finalAvailableMonster

def checkStamina(stamina, maxStamina):

    finalStamina = stamina.copy()

    if finalStamina[np.argmax(finalStamina)] > maxStamina:
        finalStamina[np.argmax(finalStamina):] = maxStamina
    
    return finalStamina
