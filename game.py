from stategies import cheat, cooperate, Strategy, DoubleCooperate, CopyOpponent, RandomChoice

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
    print(f"Average games score {avg_player1}, all games score {player1.game_scores}for strategy {player1.name} ")
    print(f"Average games score {avg_player2}, all games score {player2.game_scores}for strategy {player2.name} ")


if __name__ == '__main__':
    players = {DoubleCooperate.name: lambda: DoubleCooperate(),
               CopyOpponent.name: lambda: CopyOpponent(),
               RandomChoice.name: lambda: RandomChoice()}
    names = [DoubleCooperate.name, CopyOpponent.name, RandomChoice.name]

    for name in names:
        for name2 in names:
            play(players[name](), players[name2]())
