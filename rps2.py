import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def __init__(self):
        self.score = 0
        self.their_move = None
        self.my_move = None


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def __init__(self):
        self.score = 0


class HumanPlayer(Player):
    def move(self):
        choice = input("Rock, Paper, Scissors? >")
        choice = choice.lower()
        while True:
            if choice in moves:
                return choice
            elif choice == "quit":
                break
            else:
                choice = input("Rock, Paper, Scissors? >")


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            return moves[(moves.index(self.my_move)+1) % 3]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = HumanPlayer()
        self.p2 = CyclePlayer()

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move1}. \nOpponent played {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if beats(move1, move2) is True:
            self.p1.score += 1
            print("** PLAYER ONE WINS **")
        elif beats(move2, move1) is True:
            self.p2.score += 1
            print("** PLAYER TWO WINS **")
        else:
            print("** TIE **")
        print(f"Score Player1 {self.p1.score}, Player2 {self.p2.score}\n")

    def play_game(self):
        print("Game start!\n")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        if self.p1.score > self.p2.score:
            print("Player One is the final winner!\n")
        elif self.p1.score < self.p2.score:
            print("Player Two is the final winner\n")
        else:
            print("TIE! Everyone is a winner!")
        print("Game over!")


if __name__ == '__main__':
    game = Game(Player(), Player())
    game.play_game()
