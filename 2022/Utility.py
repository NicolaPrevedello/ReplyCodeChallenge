from collections import defaultdict

import numpy as np


def scoreFunction(availableMonster, monsterDesc, rewardList, remainingRounds):

    rewardSumList = np.zeros(len(availableMonster))
    for i in range(len(availableMonster)):
        rewardSumList[i] = np.sum(rewardList[availableMonster[i]][:remainingRounds])

    #LA SOMMA DELLE REWARD NON BASTA A DEFINIRE LO SCORE... DA COMPLETARE

    return rewardSumList


def cut_reward_list_from_current_round_and_number_of_rounds(round, reward_list, total_number_of_rounds):
    remaining_rounds = total_number_of_rounds - round
    if len(reward_list) > remaining_rounds:
        return reward_list[:remaining_rounds]

    # se la reward_list è piu piccola del numero totale di round ancora disponibili
    # allora aggiungo rewards 0 in modo da non avere problemi nel calcolo della scoring_function
    rew_list = np.zeros(remaining_rounds)
    rew_list[:len(reward_list)] = reward_list
    return rew_list


def find_highest_reward_from_first_N_rounds(N, round_number, reward_list, total_number_of_rounds):
    # taglio la lista delle rewards se il numero di round disponibili è più basso del round attuale
    normalized_rewards_list = cut_reward_list_from_current_round_and_number_of_rounds(round_number, reward_list,
                                                                                      total_number_of_rounds)
    return sum(normalized_rewards_list[:N])


def find_highest_reward_from_first_3_rounds(round_number, reward_list, total_number_of_rounds):
    return find_highest_reward_from_first_N_rounds(3, round_number, reward_list, total_number_of_rounds)


def find_single_highest_reward_from_monster(round_number, reward_list, total_number_of_rounds):
    normalized_reward_list = cut_reward_list_from_current_round_and_number_of_rounds(round_number, reward_list, total_number_of_rounds)
    # da gestire il caso in cui ci siano più indici nello stesso array con valore massimo
    max_index = np.array(normalized_reward_list).argmax()
    return normalized_reward_list[max_index], max(normalized_reward_list)


def weightedScoreFunction(round_number, available_monsters, monster_desc, monsters_rewards, total_number_of_rounds):
    # supponiamo che l'available_monsters_reward_list abbia gli stessi indici della mappa dei mostri
    weightedScore = defaultdict(None)

    # ho pensato ad una funzione tipo DCG che regolasse la gestione delle rewards:
    # https: // en.wikipedia.org / wiki / Discounted_cumulative_gain
    # altra logica invece che potrebbe essere applicata:
    # se c'è un mostro che ha rewards altissime verso la fine ma che all'inizio invece vale poco conviene comunque farlo all'inizio se ci si arriva
    monster_index_penalty = defaultdict(None)
    monster_index_acquired_score_before_max = defaultdict(None)
    monster_index_max_score = defaultdict(None)
    for i, available_monster in enumerate(available_monsters):
        turns_penalty, max_score = find_single_highest_reward_from_monster(round_number, monsters_rewards[i], total_number_of_rounds)
        monster_index_penalty[i] = turns_penalty
        # in questo modo potremmo applicare una forma di DCG
        monster_index_acquired_score_before_max[i] = cut_reward_list_from_current_round_and_number_of_rounds(0, monsters_rewards[i], turns_penalty)
        monster_index_max_score[i] = max_score

    # qui si dovrebbe ragionare per inserire il tutto in una funzione peso che insieme alle penalty andrebbe a
    # creare un punteggio per ogni mostro
    penalty_factor = -0.2
    max_score = 0.4

    # moltiplicare i fattori che abbiamo scelto per il punteggio del mostro e guardare quello che ha il punteggio
    # migliore

    # l'indice del mostro avente punteggio massimo
    return 0

    # for i, available_monster in enumerate(available_monsters):
    #     weightedScore[i] = find_highest_reward_from_first_3_rounds(round_number, monsters_rewards[i], total_number_of_rounds)

