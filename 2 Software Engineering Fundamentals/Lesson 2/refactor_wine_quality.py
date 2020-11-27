# -----------------------------------------------------------------------------
# Refactor code: Wine quality analysis
# -----------------------------------------------------------------------------
# In this exercise, code is refactored that analyzes a wine quality dataset
# taken from the UCI Machine Learning Repository
# (https://archive.ics.uci.edu/ml/datasets/wine+quality). Each row contains
# data on a wine sample, including several physio chemical properties gathered
# from tests, as well as a quality rating evaluated by wine experts.
# -----------------------------------------------------------------------------
import pandas as pd

# -----------------------------------------------------------------------------
# Define user parameters
# -----------------------------------------------------------------------------
root_path = 'C:/Users/Benjamin/Development/' \
            + 'Nanodegree Machine Learning Engineer/' \
            + '2 Software Engineering Fundamentals'

# -----------------------------------------------------------------------------
# Import file
# -----------------------------------------------------------------------------
df = pd.read_csv(root_path + '/Data/wine-quality-red.csv', sep=';')

# -----------------------------------------------------------------------------
# Prepare dataframe
# -----------------------------------------------------------------------------
df.columns = [label.replace(' ', '_') for label in df.columns]
print(df.head())

# -----------------------------------------------------------------------------
# Define functions
# -----------------------------------------------------------------------------
def categorize(label):
    """
    Categorize numerical label.
    
    Args:
    label (int or float): Categorizes label 'high' or 'low' depending if
    above median or below.
    
    Returns:
    no returns. Function makes the categorization directly on the dataframe df.
    """
    median_label = df[label].median()
    for i, value in enumerate(df[label]):
        if value >= median_label:
            df.loc[i, label] = 'high'
        else:
            df.loc[i, label] = 'low'

# -----------------------------------------------------------------------------
# Analyze features
# -----------------------------------------------------------------------------
for label in df.columns[1:-1]:
    categorize(label)
    print(df.groupby(label).quality.mean(), '\n')
