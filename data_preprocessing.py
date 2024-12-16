import pandas as pd # type: ignore
import numpy as np # type: ignore

def preprocess_data(file_path):
    """
    Preprocesses the Titanic dataset:
    - Loads the dataset from the specified file path
    - Handles missing values
    - Encodes categorical variables
    - Drops unnecessary columns
    
    Parameters:
        file_path (str): Path to the Titanic dataset (CSV file).
    
    Returns:
        pd.DataFrame: The cleaned dataset ready for machine learning.
    """
    try:
        # Load the dataset
        data = pd.read_csv(file_path)
        print("Dataset loaded successfully!")

        # Handle missing values
        data['Age'] = data['Age'].fillna(data['Age'].mean())
        data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])

        # Convert categorical columns to numeric using one-hot encoding
        data = pd.get_dummies(data, columns=['Sex', 'Embarked'], drop_first=True)

        # Drop unnecessary columns
        data = data.drop(columns=['Name', 'Ticket', 'Cabin', 'PassengerId'], errors='ignore')

        print("Data preprocessing completed successfully!")
        return data

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred during preprocessing: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    file_path = "data/titanic.csv"  # Update with the actual path to the Titanic dataset
    processed_data = preprocess_data(file_path)

    if processed_data is not None:
        # Save the processed data to a new CSV file
        processed_data.to_csv("data/processed_titanic.csv", index=False)
        print("Processed data saved to 'data/processed_titanic.csv'.")

