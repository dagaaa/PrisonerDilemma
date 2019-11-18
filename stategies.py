import random

cheat = 1
cooperate = 0


class Strategy:
    name = None

    def __init__(self):
        self.history = []
        self.oponent = None
        self.score = 0
        self.game_scores = []

    def set_oponent(self, oponent):
        self.oponent = oponent
        self.score = 0
        self.game_scores = []
        self.history = []

    def move(self):
        pass

    def update(self, score, last_move):
        self.history.append(last_move)
        self.score += score

    def reset_and_start_new(self):
        self.game_scores.append(self.score)
        self.score = 0
        self.history = []

    def get_name(self):
        pass


class DoubleCooperate(Strategy):
    name = "DoubleCooperate"

    def move(self):
        if len(self.history) < 2:
            return self.first_move()
        else:
            return self.nth_move()

    def first_move(self):
        if random.random() > 0.5:
            return cheat
        return cooperate

    def nth_move(self):
        if self.oponent.history[-2:] == [cooperate, cooperate]:
            return cooperate

        return cheat


class RandomChoice(Strategy):
    name = "RandomChoice"

    def move(self):
        if random.random() > 0.5:
            return cheat
        return cooperate


class CopyOpponent(Strategy):
    name = "CopyOpponent"

    def move(self):
        if len(self.history) < 1:
            return cooperate
        else:
            return self.nth_move()

    def nth_move(self):
        if self.oponent.history[-1] == [cooperate]:
            return cooperate

        return cheat


class Cheater(Strategy):
    name = "Cheater"

    def move(self):
        return cheat


class Pavlov(Strategy):
    name = "Pavlov"

    def move(self):
        if len(self.history) == 0:
            return cooperate
        if self.history[-1] == self.oponent.history[-1]:
            return cooperate
        else:
            return cheat
