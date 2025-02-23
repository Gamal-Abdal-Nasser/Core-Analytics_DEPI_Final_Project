import os
import pandas as pd
from google.colab import files
import shutil

# Step 1: Upload the dataset manually in Colab
print("📤 Please upload the railway.csv file:")
uploaded = files.upload()

# Step 2: Get the correct filename dynamically
uploaded_filename = list(uploaded.keys())[0]

# Step 3: Define destination path
destination_path = "/content/railway_cleaned.csv"

# Step 4: Move the uploaded file to the correct path
shutil.move(uploaded_filename, destination_path)
print(f"✅ File moved successfully: {destination_path}")

# Step 5: Load the dataset
if os.path.exists(destination_path):
    railway_df = pd.read_csv(destination_path)
    print("✅ File loaded successfully!")
else:
    raise FileNotFoundError(f"❌ File not found: {destination_path}")

# Step 6: Data Cleaning
# 1️⃣ Standardize column names (remove spaces, lowercase format)
railway_df.columns = railway_df.columns.str.strip().str.lower().str.replace(" ", "_")

# 2️⃣ Drop duplicate rows
railway_df.drop_duplicates(inplace=True)

# 3️⃣ Handle missing values
# Fill missing text values with "Unknown" and missing numeric values with 0
for col in railway_df.columns:
    if railway_df[col].dtype == "object":
        railway_df[col].fillna("Unknown", inplace=True)
    else:
        railway_df[col].fillna(0, inplace=True)

# Step 7: Save and Download the Cleaned File
cleaned_data_path = "/content/railway_cleaned.csv"
railway_df.to_csv(cleaned_data_path, index=False)

print(f"✅ Cleaned data saved to {cleaned_data_path}")

# Step 8: Provide a Download Link
print("📥 Click the link below to download the cleaned file:")
print(f"[Download Cleaned Data](railway_cleaned.csv)")

# Automatically trigger the download
files.download(cleaned_data_path)
