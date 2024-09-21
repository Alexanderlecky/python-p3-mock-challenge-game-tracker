class Game:
    def __init__(self, title):
        if not isinstance(title, str) or not title:
            raise ValueError("Title must be a non-empty string")
        self._title = title
        self._results = []

    @property
    def title(self):
        return self._title

    def add_result(self, result):
        if not isinstance(result, Result):
            raise TypeError("Result must be of type Result")
        self._results.append(result)

    def results(self):
        return self._results

    def players(self):
        return list({result.player for result in self._results})

    def average_score(self, player):
        player_results = [result.score for result in self._results if result.player == player]
        if not player_results:
            return None
        return sum(player_results) / len(player_results)


class Player:
    def __init__(self, username):
        if not isinstance(username, str) or not (2 <= len(username) <= 16):
            raise ValueError("Username must be a string between 2 and 16 characters")
        self.username = username
        self._results = []

    def add_result(self, result):
        if not isinstance(result, Result):
            raise TypeError("Result must be of type Result")
        self._results.append(result)

    def results(self):
        return self._results

    def games_played(self):
        return list({result.game for result in self._results})

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return len([result for result in self._results if result.game == game])


class Result:
    all = []

    def __init__(self, player, game, score):
        if not isinstance(player, Player):
            raise TypeError("Player must be of type Player")
        if not isinstance(game, Game):
            raise TypeError("Game must be of type Game")
        if not isinstance(score, int) or not (1 <= score <= 5000):
            raise ValueError("Score must be an integer between 1 and 5000")
        
        self._score = score
        self.player = player
        self.game = game
        Result.all.append(self)  # Register this result

    @property
    def score(self):
        return self._score
