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
            row = list(filter(bool, row))
            #print("Line {}: {}".format(cnt, row))
            if cnt == 0:
                startStamina = int(row[0])
                maxStamina = int(row[1])
                totalRounds = int(row[2])
                monsterToFace = int(row[3])   

            if cnt != 0:
                monsterDesc[cnt-1, :]= row[0:4]
                if len(row) == 4:
                    rewardList.append(np.zeros(totalRounds))
                elif(len(row)<totalRounds):
                    rewardList.append(np.pad(np.asarray(row[4:], dtype=int),(0, totalRounds-(len(row)-4) ) ))
                else:
                    rewardList.append(np.asarray(row[4:], dtype=int))

            cnt += 1 

    # print("startStamina: ", startStamina)
    # print("maxStamina: ", maxStamina)
    # print("totalRounds: ", totalRounds)
    # print("monsterToFace: ", monsterToFace)
    # print("monsterDesc: ")
    # print(monsterDesc)
    # print("rewardList: ")
    # print(rewardList)

    return startStamina,maxStamina,totalRounds,monsterToFace,monsterDesc,rewardList