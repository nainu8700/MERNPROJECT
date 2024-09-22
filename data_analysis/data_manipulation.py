import pandas as pd

def get_top_5_by_age(df, age_threshold=30):
    # Filter rows where age is greater than the threshold
    filtered_df = df[df['age'] > age_threshold]
    
    # Sort by age descending and return top 5
    return filtered_df.sort_values('age', ascending=False).head()

if __name__ == "__main__":
    # Read the CSV file
    df = pd.read_csv("input.csv")
    
    # Get and print the result
    result = get_top_5_by_age(df)
    print("Top 5 rows where age > 30:")
    print(result)