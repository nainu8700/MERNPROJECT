import pandas as pd

def clean_data(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Print original shape
    print(f"Original data shape: {df.shape}")
    
    # Drop rows with missing values
    df_cleaned = df.dropna()
    
    # Print cleaned shape
    print(f"Cleaned data shape: {df_cleaned.shape}")
    
    # Output the cleaned data
    df_cleaned.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    clean_data("input.csv", "cleaned_output.csv")