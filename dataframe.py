# ------------------------------------------------------------------------------
# Imports

import pandas as pd

# ------------------------------------------------------------------------------
# Dictionary Data

test_scores = {
    'person': ['Rishab', 'Hitesh', 'Vinny', 'Rony'],
    'score': [100, 43, 93, 29],
    'time studied': [3, 45, 28, 10],
    'date': ['1/1/2009', '3/29/2018', '4/4/2008', '1/31/2004']
}

df = pd.DataFrame(test_scores)


# -----------------------
# Merge

df2 = {
    'person' : ['Rishab', 'Hitesh', 'Jamie', 'Ishy', ],
    'score' : [100, 43, 67, 23],
    'time studied' : [1, 48, 30, 35],
    'date' : ['1/1/2009', '3/29/2019', '4/5/2012', '5/29/2022']
}

merge = pd.merge(df, df2, how='outer', indicator=True)
print(merge)
