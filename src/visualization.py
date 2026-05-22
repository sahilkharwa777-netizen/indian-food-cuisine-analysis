import matplotlib.pyplot as plt
import seaborn as sns


# -----------------------------------
# Rating Distribution Plot
# -----------------------------------

def plot_rating_distribution(df):

    plt.figure(figsize=(10, 6))

    sns.histplot(
        df['Ratings_of_Dish'],
        bins=20,
        kde=True
    )

    plt.title("Distribution of Dish Ratings")
    plt.xlabel("Ratings")
    plt.ylabel("Frequency")

    plt.savefig(
        "outputs/plots/rating_distribution.png"
    )

    plt.close()

    print(" Rating Distribution Plot Saved!")


# -----------------------------------
# Complexity Comparison Plot
# -----------------------------------

def plot_complexity(df):

    plt.figure(figsize=(10, 6))

    sns.boxplot(
        x='Diet_Type',
        y='Complexity_Score',
        data=df
    )

    plt.xticks(rotation=45)

    plt.title("Complexity Score by Diet Type")

    plt.savefig(
        "outputs/plots/complexity_plot.png"
    )

    plt.close()

    print(" Complexity Plot Saved!")


# -----------------------------------
# Cooking Time Plot
# -----------------------------------

def plot_cooking_time(df):

    cooking_data = df.groupby(
        'Diet_Type'
    )['Cooking_time'].mean()

    plt.figure(figsize=(12, 6))

    cooking_data.plot(kind='bar')

    plt.title("Average Cooking Time by Diet Type")

    plt.xlabel("Diet Type")
    plt.ylabel("Cooking Time")

    plt.xticks(rotation=45)

    plt.savefig(
        "outputs/plots/cooking_time_plot.png"
    )

    plt.close()

    print(" Cooking Time Plot Saved!")


# -----------------------------------
# Cuisine Distribution Plot
# -----------------------------------

def plot_cuisine_distribution(df):

    plt.figure(figsize=(12, 6))

    top_cuisines = df['Cuisine_name'].value_counts().head(10)

    top_cuisines.plot(kind='bar')

    plt.title("Top 10 Cuisine Types")

    plt.xlabel("Cuisine")
    plt.ylabel("Count")

    plt.xticks(rotation=45)

    plt.savefig(
        "outputs/plots/cuisine_distribution.png"
    )

    plt.close()

    print(" Cuisine Distribution Plot Saved!")