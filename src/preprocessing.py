import pandas as pd


def clean_data(df):

    # Remove extra spaces from column names
    df.columns = df.columns.str.strip()

    print("\n Cleaned Column Names:\n")
    print(df.columns)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove rows with missing dish names
    df = df.dropna(subset=['name_of_Dish'])

    # Fill missing cuisine names
    df['Cuisine_name'] = df['Cuisine_name'].fillna("Unknown")

    # Fill missing diet types
    df['Diet_Type'] = df['Diet_Type'].fillna("Unknown")

    # Convert ratings into numeric
    df['Ratings_of_Dish'] = pd.to_numeric(
        df['Ratings_of_Dish'],
        errors='coerce'
    )

    # Fill missing ratings with mean
    df['Ratings_of_Dish'] = df['Ratings_of_Dish'].fillna(
        df['Ratings_of_Dish'].mean()
    )

    # Time columns
    time_columns = [
    'Prepration_time',
    'Cooking_time',
    'Total_time'
]

    # Convert time columns into numeric
    for col in time_columns:

        if col in df.columns:

            df[col] = pd.to_numeric(
                df[col],
                errors='coerce'
            )

            df[col] = df[col].fillna(
                df[col].median()
            )

        else:
            print(f"\n Column not found: {col}")

    print("\n Data cleaned successfully!\n")

    return df