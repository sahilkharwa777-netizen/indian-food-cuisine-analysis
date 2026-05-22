import pandas as pd

def load_dataset(file_path):
    try:
        df = pd.read_excel(file_path)

        print("\n Dataset loaded successfully!\n")

        return df

    except Exception as e:
        print(" Error loading dataset:", e)