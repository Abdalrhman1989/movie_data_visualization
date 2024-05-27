import pandas as pd

def load_data(file_path):
    """Load data from a CSV file."""
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    """Clean and preprocess the data."""
    clean_data = data.dropna()
    return clean_data
