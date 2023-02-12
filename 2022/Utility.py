import numpy as np


def scoreFunction(availableMonster, monsterDesc, rewardList, remainingRounds):

    rewardSumList = np.zeros(len(availableMonster))
    for i in range(len(availableMonster)):
        rewardSumList[i] = np.sum(rewardList[availableMonster[i]][:remainingRounds])

    #LA SOMMA DELLE REWARD NON BASTA A DEFINIRE LO SCORE... DA COMPLETARE

    return rewardSumList