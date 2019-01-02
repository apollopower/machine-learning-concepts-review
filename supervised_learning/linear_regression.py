import pandas as pd

# Filepath to data
file_path = '../data/world_happiness_report.csv'

# Reading Data
report = pd.read_csv(file_path)

print(report.head())