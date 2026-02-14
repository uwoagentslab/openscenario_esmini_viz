from datasets import load_dataset
import pandas as pd

# Load the dataset
dataset = load_dataset("Ammara66/openscenario-dataset")

# Explore the dataset structure
print("Dataset structure:")
print(dataset)
print("\n" + "="*80 + "\n")

# Check the first few examples
if 'train' in dataset:
    df = pd.DataFrame(dataset['train'])
    print(f"Number of rows: {len(df)}")
    print(f"\nColumns: {df.columns.tolist()}")
    print("\nFirst few rows:")
    print(df.head())
    
    # Save to CSV for easier inspection
    df.to_csv('dataset_sample.csv', index=False)
    print("\nDataset saved to dataset_sample.csv")
    
    # Show a sample scenario
    if len(df) > 0:
        print("\n" + "="*80)
        print("Sample scenario:")
        print("="*80)
        for col in df.columns:
            print(f"\n{col}:")
            print(df.iloc[0][col])
