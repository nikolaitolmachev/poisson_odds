# Odds by Poisson Distribution
This library enables the calculation of betting odds (moneyline, handicaps, totals) based on team qualities using the Poisson distribution.

It provides a simple interface for initializing calculations, requiring only the qualities of both teams. These qualities can be obtained using metrics such as expected goals (xG) or average number of goals.

## Installation
```
pip install poisson-odds
```

## Usage Example
```
from poisson_odds import *

test = Poisson(1.1, 2.1)

test.print_probability_table_goal_draws()
### Output:
```
![Probability Table](src/prob_table.jpg)
```
print(test.moneyline)

### Output:
```
```
1-X-2: 5.291-4.878-1.669
```
```
handicaps = test.calculate_handicap_odds_by_Poisson()
print('\n'.join([str(items) for key, items in handicaps.items()]))
### Output:
```
```
...
0.75: 2.206 / 1.879
1.0: 1.918 / 2.089
1.25: 1.75 / 2.403
1.5: 1.582 / 2.717
...
```
```
totals = test.calculate_total_odds_by_Poisson()
print('\n'.join([str(items) for key, items in totals.items()]))
### Output:
```
```
...
Over/Under 2.75: 1.788 / 2.333
Over/Under 3: 1.961 / 2.04
Over/Under 3.25: 2.243 / 1.848
Over/Under 3.5: 2.525 / 1.656
...
```


