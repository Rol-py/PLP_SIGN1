# Assignment: Analyzing Data with Pandas & Visualizing Results with Matplotlib

# -------------------------------
# Step 0: Import Libraries
# -------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# -------------------------------
# Step 1: Load and Explore Dataset
# -------------------------------

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Explore structure and missing values
print("\nDataset Info:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

# Clean missing values if any (none in Iris dataset, just for demonstration)
df = df.dropna()  # or df.fillna(value)

# -------------------------------
# Step 2: Basic Data Analysis
# -------------------------------

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Grouping by species and computing mean of numerical columns
species_mean = df.groupby("species").mean()
print("\nMean values by species:")
print(species_mean)

# Observations
print("\nObservations:")
print("1. Setosa generally has smaller sepal and petal lengths than versicolor and virginica.")
print("2. Virginica tends to have the largest petal and sepal measurements.")

# -------------------------------
# Step 3: Data Visualization
# -------------------------------

# 1️⃣ Line Chart: Sepal length trend for all species
plt.figure(figsize=(8,5))
for species in df['species'].unique():
    plt.plot(df[df['species']==species]['sepal length (cm)'].values, label=species)
plt.title("Sepal Length Trend by Species")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2️⃣ Bar Chart: Average Petal Length per Species
plt.figure(figsize=(6,4))
species_mean['petal length (cm)'].plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon'])
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3️⃣ Histogram: Distribution of Sepal Width
plt.figure(figsize=(6,4))
plt.hist(df['sepal width (cm)'], bins=10, color='purple', edgecolor='black')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4️⃣ Scatter Plot: Petal Length vs Petal Width
plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x='petal length (cm)', y='petal width (cm)', hue='species', palette='Set1')
plt.title("Petal Length vs Petal Width by Species")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.legend()
plt.show()
