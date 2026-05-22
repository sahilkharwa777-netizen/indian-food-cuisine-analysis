from src.visualization import (
    plot_rating_distribution,
    plot_complexity,
    plot_cooking_time,
    plot_cuisine_distribution
)
from src.data_loader import load_dataset
from src.preprocessing import clean_data

from src.analysis import (
    analyze_rating_distribution,
    calculate_complexity_score,
    compare_cuisine_complexity,
    analyze_cooking_time_variation,
    count_special_diets,
    most_common_cuisine_by_course
)

# Dataset path
file_path = "data/Python_Dataset.xlsx"

# Load dataset
df = load_dataset(file_path)

# Clean dataset
df = clean_data(df)

# Calculate complexity score
df = calculate_complexity_score(df)

# -----------------------------------
# QUESTION 1
# -----------------------------------
analyze_rating_distribution(df)

# -----------------------------------
# QUESTION 2
# -----------------------------------
compare_cuisine_complexity(df)

# -----------------------------------
# QUESTION 3
# -----------------------------------
analyze_cooking_time_variation(df)

# -----------------------------------
# QUESTION 4
# -----------------------------------
count_special_diets(df)

# -----------------------------------
# QUESTION 5
# -----------------------------------
most_common_cuisine_by_course(df)
# -----------------------------------
# VISUALIZATIONS
# -----------------------------------

plot_rating_distribution(df)

plot_complexity(df)

plot_cooking_time(df)

plot_cuisine_distribution(df)
