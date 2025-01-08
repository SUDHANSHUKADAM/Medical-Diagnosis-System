import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
covid_df = pd.read_csv(r'C:\SUDHA\Personal portfolio project\datasets\covid.csv')
diabetes_df = pd.read_csv(r'C:\SUDHA\Personal portfolio project\datasets\diabetes.csv')
heart_disease_df = pd.read_csv(r'C:\SUDHA\Personal portfolio project\datasets\heart_disease_uci.csv')


# --- COVID-19 Dataset Visualization ---
# Symptom Frequency
symptoms = covid_df.iloc[:, :9].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=symptoms.values, y=symptoms.index, palette="coolwarm")
plt.title("Frequency of Symptoms in COVID-19 Dataset", fontsize=16)
plt.xlabel("Frequency", fontsize=12)
plt.ylabel("Symptoms", fontsize=12)
plt.show()

# --- Diabetes Dataset Visualization ---
# Distribution of Glucose Levels
plt.figure(figsize=(10, 6))
sns.histplot(diabetes_df['Glucose'], kde=True, color="skyblue", bins=30)
plt.title("Distribution of Glucose Levels", fontsize=16)
plt.xlabel("Glucose", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.show()

# Correlation Heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(diabetes_df.corr(), annot=True, cmap="YlGnBu", fmt=".2f")
plt.title("Correlation Heatmap of Diabetes Dataset", fontsize=16)
plt.show()

# --- Heart Disease Dataset Visualization ---
# Age Distribution
plt.figure(figsize=(10, 6))
sns.histplot(heart_disease_df['age'], kde=True, color="orange", bins=20)
plt.title("Age Distribution of Heart Disease Patients", fontsize=16)
plt.xlabel("Age", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.show()

# Chest Pain Type by Diagnosis
plt.figure(figsize=(10, 6))
sns.countplot(data=heart_disease_df, x='cp', hue='num', palette="viridis")
plt.title("Chest Pain Type by Diagnosis", fontsize=16)
plt.xlabel("Chest Pain Type", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.legend(title="Diagnosis (0: No Disease, 1+: Disease)")
plt.show()