import pandas as pd
import os

data_path = "data/iris/iris.data"
column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
iris_data = pd.read_csv(data_path, names=column_names)

if not os.path.exists('results/'):
    os.makedirs('results/', exist_ok=True)

def compute_summary_stats(df, flower_type):
    flower_data = df[df["class"] == flower_type]
    summary_stats = flower_data.describe()
    return summary_stats

flower_types = iris_data["class"].unique()

for flower_type in flower_types:
    flower_summary = compute_summary_stats(iris_data, flower_type)
    output_path = os.path.join("results/", f"{flower_type}_summary.txt")

    with open(output_path, "w") as file:
        file.write(f"Summary Statistics for {flower_type}:\n\n")
        file.write(f"{flower_summary}\n\n")

print("Summary statistics for each flower type have been computed and saved in the 'results/' directory.")
