import poisson_odds.consts as consts

class BookmakerTotal:
    """
    Describes a bookmaker total.

    :var line: line of total.
    :var odds_over: odds for Over.
    :var odds_under: odds for Under.
    """

    def __init__(self, line: float, odds_over: float, odds_under: float):
        self.__line = line
        self.__odds_over = odds_over
        self.__odds_under = odds_under

    @property
    def line(self) -> float:
        return self.__line
    @property
    def odds_over(self) -> float:
        return self.__odds_over
    @property
    def odds_under(self) -> float:
        return self.__odds_under

    def __str__(self):
        return 'Over/Under {}: {} / {}'.format(self.__line, self.__odds_over, self.__odds_under)

    def __lt__(self, other):
        return self.__line < other.line

    def __gt__(self, other):
        return self.__line > other.line

    @staticmethod
    def get_only_meaningful_lines(totals: list) -> list:
        return [total for total in totals if total.odds_over >= consts.MIN_ODDS_TO_LINES and
                total.odds_under >= consts.MIN_ODDS_TO_LINES]