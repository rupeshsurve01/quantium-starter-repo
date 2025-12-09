import pandas as pd
import os

data_folder = "data"
all_data = []

for file in os.listdir(data_folder):
    if file.endswith(".csv"):
        file_path = os.path.join(data_folder, file)
        df = pd.read_csv(file_path)

        # Clean product column
        df["product"] = df["product"].astype(str).str.strip().str.lower()

        # Keep only pink morsel
        df = df[df["product"] == "pink morsel"]

        # ✅ CLEAN PRICE (remove $ sign and convert to number)
        df["price"] = df["price"].astype(str).str.replace("$", "", regex=False)
        df["price"] = pd.to_numeric(df["price"], errors="coerce")

        # ✅ Convert quantity to number
        df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

        # ✅ NOW calculate Sales correctly
        df["Sales"] = df["quantity"] * df["price"]

        # Keep only required columns
        df = df[["Sales", "date", "region"]]

        all_data.append(df)

# Combine all data
final_df = pd.concat(all_data, ignore_index=True)

# Remove any bad rows
final_df = final_df.dropna(subset=["Sales", "date"])

# Save output
final_df.to_csv("final_output.csv", index=False)

print("✅ final_output.csv created successfully!")
print(final_df.head())
