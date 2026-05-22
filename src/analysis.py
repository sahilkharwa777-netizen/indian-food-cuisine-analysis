import pandas as pd


# -----------------------------------
# Question 1
# Rating Distribution Analysis
# -----------------------------------

def analyze_rating_distribution(df):

    print("\n========== QUESTION 1 ==========")

    high_protein_veg = df[
        df['Diet_Type'].str.contains(
            'High Protein Vegetarian',
            case=False,
            na=False
        )
    ]

    high_protein_nonveg = df[
        df['Diet_Type'].str.contains(
            'High Protein Non Vegetarian',
            case=False,
            na=False
        )
    ]

    print("\nHigh Protein Vegetarian Average Rating:")
    print(high_protein_veg['Ratings_of_Dish'].mean())

    print("\nHigh Protein Non Vegetarian Average Rating:")
    print(high_protein_nonveg['Ratings_of_Dish'].mean())


# -----------------------------------
# Question 2
# Dish Complexity
# -----------------------------------

def calculate_complexity_score(df):

    ingredient_count = df['Ingredients_of_Dish'].apply(
        lambda x: len(str(x).split(','))
    )

    df['Complexity_Score'] = (
        (ingredient_count * 1)
        + (df['Prepration_time'] * 0.3)
        + (df['Cooking_time'] * 0.7)
    )

    print("\n Complexity Score Calculated!")

    return df


def compare_cuisine_complexity(df):

    print("\n========== QUESTION 2 ==========")

    highly_rated = df[df['Ratings_of_Dish'] > 4.5]

    indian = highly_rated[
        highly_rated['Cuisine_name'].str.contains(
            'Indian',
            case=False,
            na=False
        )
    ]

    international = highly_rated[
        ~highly_rated['Cuisine_name'].str.contains(
            'Indian',
            case=False,
            na=False
        )
    ]

    print("\nAverage Indian Cuisine Complexity:")
    print(indian['Complexity_Score'].mean())

    print("\nAverage International Cuisine Complexity:")
    print(international['Complexity_Score'].mean())


# -----------------------------------
# Question 3
# Cooking Time Variation
# -----------------------------------

def analyze_cooking_time_variation(df):

    print("\n========== QUESTION 3 ==========")

    cooking_variation = df.groupby(
        'Diet_Type'
    )['Cooking_time'].max()

    print(cooking_variation)


# -----------------------------------
# Question 4
# Diabetic-Friendly & Sugar-Free
# -----------------------------------

def count_special_diets(df):

    print("\n========== QUESTION 4 ==========")

    diabetic_count = df[
        df['Diet_Type'].str.contains(
            'Diabetic',
            case=False,
            na=False
        )
    ].shape[0]

    sugar_free_count = df[
        df['Diet_Type'].str.contains(
            'Sugar Free',
            case=False,
            na=False
        )
    ].shape[0]

    print("\nDiabetic Friendly Dishes:")
    print(diabetic_count)

    print("\nSugar Free Dishes:")
    print(sugar_free_count)


# -----------------------------------
# Question 5
# Most Common Cuisine Per Course
# -----------------------------------

def most_common_cuisine_by_course(df):

    print("\n========== QUESTION 5 ==========")

    result = df.groupby(
        'Course_name'
    )['Cuisine_name'].agg(
        lambda x: x.mode()[0]
    )

    print(result)