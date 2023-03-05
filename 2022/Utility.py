import os
import numpy as np

#Calcolo la somma delle reward della lista degli availableMonster dal turno attuale fino alla fine
def rankFunction(availableMonster, rewardList, remainingRounds):

    rewardSumList = np.zeros(len(availableMonster))
    for i in range(len(availableMonster)):
        rewardSumList[i] = np.sum(rewardList[availableMonster[i]][:remainingRounds])

    return rewardSumList


""" 
Questa funzione calcola il valore della soluzione passata (monsterList).
La monsterList che riceve deve avere un mostro per turno, se in un turno non si è preso nessun mostro va messo un -1 
"""
def solutionFinalScore(monsterList, rewardList):
    scorePerRound =  np.zeros(len(monsterList))
    for i in range(len(monsterList)):
        if(monsterList[i]>=0):
            scorePerRound[i:] += rewardList[monsterList[i]][:len(monsterList)-i]

    return np.sum(scorePerRound)


#Salva la soluzione in un file di testo
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


#Vengono rimossi dalla lista degli availableMonster i mostri già affrontati in passato
def removeAlreadyDefeated(availableMonster, actualSolution):

    finalAvailableMonster = availableMonster.copy()

    for i in range(len(availableMonster)):
        if availableMonster[i] in actualSolution:
            finalAvailableMonster.remove(availableMonster[i])
    
    return finalAvailableMonster


#Viene controllato che la stamina non ecceda il valore massimo
def checkStamina(stamina, maxStamina):

    finalStamina = stamina.copy()

    if finalStamina[np.argmax(finalStamina)] > maxStamina:
        finalStamina[np.argmax(finalStamina):] = maxStamina
    
    return finalStamina
