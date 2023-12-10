## Retail Sales Prediction Project

# Overview
Predict retail sales using historical data and store features. The project includes data merging, cleaning, exploratory data analysis (EDA), and building predictive models.

# Project Structure
# Data Files:

sales_data_set.csv: Weekly sales, store, department, date, and holiday information.
features_data_set.csv: Features like temperature, fuel price, markdowns, CPI, unemployment, and holidays.
stores_data_set.csv: Store information, including type and size.
# Code Files:

merge_and_clean.py: Merges datasets and performs initial cleaning.
preprocessing.py: Handles missing values and converts categorical variables.
model_building.py: Builds Random Forest, AdaBoost, and Gradient Boosting models.
# Saved Models:

sales.pkl: Trained Random Forest model for weekly sales prediction.
# Instructions
# Data Setup:

Ensure data files are present.
Run merge_and_clean.py for initial setup.
# Preprocessing:

Run preprocessing.py for missing values and categorical variables.
# Model Building:

Run model_building.py for Random Forest, AdaBoost, and Gradient Boosting models.
Trained Random Forest model is saved as sales.pkl.
# Exploratory Data Analysis:

Check EDA in the Jupyter Notebook or script.
Visualize total sales by store type and temperature vs. average sales.

![EDA](https://github.com/aravinthbalaiyan/Retail_sales_prediction/assets/144364538/03f66e53-4fb2-4eac-9b47-32b73eba4eec)

# Results:

Review cross-validation scores and model performance metrics.
# Saved Data:

Cleaned dataset: Cleaned dataset.csv.
Merged dataset: merge.csv.
# Dependencies:

Install required libraries:
Copy code
     "pip install pandas matplotlib seaborn scikit-learn"
# Notes:

Utilize the sales.pkl model for weekly sales prediction.
Further insights can be gained through EDA visualizations.
Investigate Markdown impact on sales.
## Additional Points
Explored feature importance using Random Forest.
Cleaned dataset to handle negative weekly sales values.
Utilized Heatmap for correlation analysis.
Investigated the impact of holidays on sales.
