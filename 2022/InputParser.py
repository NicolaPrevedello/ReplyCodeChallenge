import csv
import numpy as np


#Input parser

def parseInput(fileName):

    with open(fileName) as f:
        reader = csv.reader(f, delimiter=' ')

        lines = list(reader)
        linesNumber= len(lines)

        monsterDesc = np.zeros((linesNumber - 1, 4), int)
        rewardList = []

        cnt = 0
        for row in lines:
            print("Line {}: {}".format(cnt, row))
            if cnt == 0:
                startMana = int(row[0])
                maxMana = int(row[1])
                totalRounds = int(row[2])
                monsterToFace = int(row[3])   

            if cnt != 0:
                monsterDesc[cnt-1, :]= row[0:4]
                rewardList.append(np.asarray(row[4:], dtype=int))

            cnt += 1 

    print("startMana: ", startMana)
    print("maxMana: ", maxMana)
    print("totalRounds: ", totalRounds)
    print("monsterToFace: ", monsterToFace)
    print("monsterDesc: ")
    print(monsterDesc)
    print("rewardList: ")
    print(rewardList)

    return startMana,maxMana,totalRounds,monsterToFace,monsterDesc,rewardList