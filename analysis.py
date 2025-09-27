# ---- Part 1: Import Libraries ----
import pandas as pd
import matplotlib.pyplot as plt

# ---- Part 2: Load Data ----
df = pd.read_csv("metadata.csv")

# Show first few rows
print(df.head())

# ---- Part 3: Basic Data Exploration ----
print("Shape:", df.shape)
print("Data Types:\n", df.dtypes.head())
print("Missing Values:\n", df.isnull().sum().head(10))
print("Statistics:\n", df.describe())

# ---- Part 4: Data Cleaning ----
df = df.dropna(subset=["title", "abstract", "publish_time"])  # drop rows missing key info
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
df["year"] = df["publish_time"].dt.year

# ---- Part 5: Analysis ----
papers_by_year = df["year"].value_counts().sort_index()

# ---- Part 6: Visualization ----
plt.figure(figsize=(8,4))
papers_by_year.plot(kind="bar")
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Papers")
plt.show()







