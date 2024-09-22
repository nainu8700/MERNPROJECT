import pandas as pd
import numpy as np

def calculate_statistics(input_file, column='age'):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Print data info for debugging
    print("Data Info:")
    print(df.info())
    print("\nFirst few rows:")
    print(df.head())
    
    # Check for missing values
    print(f"\nMissing values in {column}:", df[column].isnull().sum())
    
    # Calculate statistics using Pandas (ignoring NaN values)
    mean = df[column].mean()
    median = df[column].median()
    std_dev = df[column].std()
    
    print(f"\nStatistics for {column} (using Pandas):")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")
    
    # Using NumPy for calculations (handling NaN values)
    np_array = df[column].to_numpy()
    np_array = np_array[~np.isnan(np_array)]  # Remove NaN values
    
    np_mean = np.mean(np_array)
    np_median = np.median(np_array)
    np_std = np.std(np_array)
    
    print(f"\nStatistics for {column} (using NumPy):")
    print(f"Mean: {np_mean:.2f}")
    print(f"Median: {np_median:.2f}")
    print(f"Standard Deviation: {np_std:.2f}")

if __name__ == "__main__":
    calculate_statistics("input.csv")