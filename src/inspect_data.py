import pandas as pd

# Load the dataset
file_path = '/Users/abdalrhmandarra/Desktop/movie_data_visualization/data/movies.csv'
data = pd.read_csv(file_path)

# Display the first few rows
print(data.head())

# Display data types
print(data.dtypes)

# Display summary statistics
print(data.describe())
