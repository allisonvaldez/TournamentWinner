"""
Allison Valdez
Time complexity: O(n) where n is the number of competitions.
Space complexity: O(k) where k is the number of k teams the 30 characters
does not matter in the analysis.
"""

home_team_won = 1


def tournament_winner(competitions, results):
    """
    The competitions and results are two different arrays that contain the
    competition details.

    about .enumerate():
    when dealing with iterators, we also get a need to keep a count of
    iterations. Python eases the programmers’ task by providing a built-in
    function enumerate() for this task. Enumerate() method adds a counter to
    an iterable and returns it in a form of enumerating object. This
    enumerated object can then be used directly for loops or converted into a
    list of tuples using the list() method.

    :param competitions: array of the competition round for each team
    :param results: array of the outcome of the competitions
    :return: the best team that won the full competition
    """
    current_best_team = ""

    scores = {current_best_team: 0}

    for index, current_round in enumerate(competitions):
        current_result = results[index]

        home_team, away_team = current_round

        winning_team = home_team if current_result == home_team_won else away_team

        update_scores(winning_team, 3, scores)

        if scores[winning_team] > scores[current_best_team]:
            current_best_team = winning_team

    return current_best_team


def update_scores(team, points, scores):
    """
    This function is in charge of checking whether we have a team or not (
    that has recently scored). If the team does not exists then we initialize
    it with a 0 score, and add their 3 points of scoring the points.

    :param team: new team that scored (not in our list of teams that competed
    :param points: the 3 points scored by the team
    :param scores: the new teams most up to date score
    :return: the new team with the correct competition outcome for the round
    """
    if team not in scores:
        scores[team] = 0

    scores[team] += points
