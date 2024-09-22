import pandas as pd
import matplotlib.pyplot as plt

def visualize_age_distribution(input_file):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Create a bar chart
    plt.figure(figsize=(10, 6))
    df['age'].value_counts().sort_index().plot(kind='bar')
    plt.title('Distribution of User Ages')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.savefig('age_distribution.png')
    plt.close()
    print("Age distribution chart saved as age_distribution.png")

if __name__ == "__main__":
    visualize_age_distribution("input.csv")