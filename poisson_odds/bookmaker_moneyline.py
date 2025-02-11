class BookmakerMoneyline:
    """
    Describes a bookmaker moneyline: 1-X-2.

    :var odds_home: odds for home win.
    :var odds_draw: odds for a draw.
    :var odds_away: odds for away win.
    """

    def __init__(self, odds_home: float, odds_draw: float, odds_away: float):
        self.__odds_home = odds_home
        self.__odds_draw = odds_draw
        self.__odds_away = odds_away

    @property
    def odds_home(self) -> float:
        return self.__odds_home

    @property
    def odds_draw(self) -> float:
        return self.__odds_draw

    @property
    def odds_away(self) -> float:
        return self.__odds_away

    def __str__(self):
        return '1-X-2: {}-{}-{}'.format(self.__odds_home, self.__odds_draw, self.__odds_away)