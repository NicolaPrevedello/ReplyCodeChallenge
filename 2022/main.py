from InputParser import parseInput
from Utility import scoreFunction, weightedScoreFunction

def pandoras_adventure():
    startMana, maxMana, totalRounds, monsterToFace, monsterDesc, rewardList = parseInput("./00-example.txt")

    # Inizio algoritmo soluzione ottima
    mana = startMana

    for i in range(totalRounds):

        # Trovo i mostri che posso affrontare
        availableMonster = []
        for j in range(monsterDesc.shape[0]):
            if (monsterDesc[j][0] < mana):
                availableMonster.append(j)

        scores = scoreFunction(availableMonster, monsterDesc, rewardList, totalRounds - i)
        print("Round {} Monsters {} scores: {}".format(i, availableMonster, scores))


def weighted_approach():
    startMana, maxMana, totalRounds, monsterToFace, monsterDesc, rewardList = parseInput("./00-example.txt")

    # Da capire come gestirlo
    mana = startMana

    for i in range(totalRounds):
        # Trovo i mostri che posso affrontare
        # availableMonster = []
        # for j in range(monsterDesc.shape[0]):
        #     if (monsterDesc[j][0] < mana):
        #         availableMonster.append(j)

        chosen_monster = weightedScoreFunction(i, monsterToFace, monsterDesc, rewardList, totalRounds)

        # calcolo dello score


if __name__ == '__main__':
    pandoras_adventure()
