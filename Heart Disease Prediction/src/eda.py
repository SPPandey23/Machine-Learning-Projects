import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd

def plot_target_distribution(df):
    df["target"].value_counts().plot(kind="bar")
    plt.title("Target Distribution")
    plt.show()

def plot_sex_distribution(df):
    pd.crosstab(df.target, df.sex).plot(kind="bar")
    plt.title("Heart Disease Frequency for Sex")
    plt.show()

def plot_age_vs_thalach(df):
    plt.scatter(df.age[df.target == 1],
                df.thalach[df.target == 1])
    plt.scatter(df.age[df.target == 0],
                df.thalach[df.target == 0])
    plt.xlabel("Age")
    plt.ylabel("Max Heart Rate")
    plt.show()

def plot_age_distribution(df):
    df.age.hist()
    plt.title("Age Distribution")
    plt.show()

def plot_cp_distribution(df):
    pd.crosstab(df.cp, df.target).plot(kind="bar")
    plt.title("Chest Pain vs Target")
    plt.show()

def plot_correlation_matrix(df):
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True)
    plt.title("Correlation Matrix")
    plt.show()

def run_eda(df):
    plot_target_distribution(df)
    plot_sex_distribution(df)
    plot_age_vs_thalach(df)
    plot_age_distribution(df)
    plot_cp_distribution(df)
    plot_correlation_matrix(df)