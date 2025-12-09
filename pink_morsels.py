import pandas as pd
import os

# Folder where CSV files are stored
data_folder = "data"

# List to store all data
all_data = []

# Read all CSV files from the data folder
for file in os.listdir(data_folder):
    if file.endswith(".csv"):
        file_path = os.path.join(data_folder, file)
        df = pd.read_csv(file_path)

        # Keep only Pink Morsels
        df = df[df["product"] == "Pink Morsels"]

        # Create Sales column
        df["Sales"] = df["quantity"] * df["price"]

        # Keep only required columns
        df = df[["Sales", "date", "region"]]

        all_data.append(df)

# Combine all three CSV files into one
final_df = pd.concat(all_data)

# Save final output file
final_df.to_csv("final_output.csv", index=False)

print("Final output file created successfully ✅")
