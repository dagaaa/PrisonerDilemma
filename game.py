from stategies import cheat, cooperate, Strategy, DoubleCooperate, CopyOpponent, RandomChoice, Cheater, Pavlov

game_score = {
    cheat: {cheat: [1, 1],
            cooperate: [5, 0]},
    cooperate: {
        cooperate: [3, 3],
        cheat: [0, 5]
    }
}


def play(player1: Strategy, player2: Strategy, games=10, iterations=100):
    player1.set_oponent(player2)
    player2.set_oponent(player1)

    for i in range(games):
        for j in range(iterations):
            player1_move = player1.move()
            player2_move = player2.move()
            score = game_score[player1_move][player2_move]
            player1.update(score[0], player1_move)
            player2.update(score[1], player2_move)

        player1.reset_and_start_new()
        player2.reset_and_start_new()

    avg_player1 = sum(player1.game_scores) / games
    avg_player2 = sum(player2.game_scores) / games
    print(f"-----Prisoner Dilemma between {player1.name} and {player2.name}-------")
    print(f"Average games score {avg_player1}, all games score {player1.game_scores} for strategy {player1.name} ")
    print(f"Average games score {avg_player2}, all games score {player2.game_scores} for strategy {player2.name} ")
    return avg_player1, avg_player2


if __name__ == '__main__':
    players = {DoubleCooperate.name: lambda: DoubleCooperate(),
               CopyOpponent.name: lambda: CopyOpponent(),
               RandomChoice.name: lambda: RandomChoice(),
               Cheater.name: lambda: Cheater(),
               Pavlov.name: lambda: Pavlov()}
    names = [Cheater.name, RandomChoice.name, CopyOpponent.name, DoubleCooperate.name,  Pavlov.name]
    scores = {}

    for i in range(len(names)):
        for j in range(i, len(names)):
            name = names[i]
            name2 = names[j]
            scores[(name, name2)] = play(players[name](), players[name2]())

    print(scores)
