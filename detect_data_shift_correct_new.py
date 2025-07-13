# Detect Data Shifts and Columns with No Data --- Created by Vaishnavii S
# This code addresses the Sweetviz `VisibleDeprecationWarning` issue dynamically

import pandas as pd
import sweetviz as sv
import matplotlib.pyplot as plt
import numpy as np  # Import NumPy to patch the issue

# Fix Sweetviz `VisibleDeprecationWarning` issue dynamically
if not hasattr(np, "VisibleDeprecationWarning"):
    np.VisibleDeprecationWarning = DeprecationWarning

def detect_data_type_inconsistencies(df):
    inconsistent_columns = []
    for column in df.columns:
        try:
            # Get unique data types in the column
            data_types = df[column].apply(type).value_counts()
            if len(data_types) > 1:
                inconsistent_columns.append(column)
                print(f'Column {column} has multiple data types: {data_types}')
        except Exception as e:
            print(f'Error processing column {column}: {e}')
    return inconsistent_columns

def detect_data_shifts(csv_file):
    # Load the CSV file
    df = pd.read_csv(csv_file)

    # Initial inspection
    print("Initial inspection:")
    print(df.head())
    print(df.info())

    # Data type consistency
    print("\nData type consistency:")
    data_types = df.dtypes
    print(data_types)

    # Null values
    print("\nNull values:")
    null_values = df.isnull().sum()
    print(null_values)

    # Value distribution
    print("\nValue distribution:")
    for column in df.columns:
        print(f'Column: {column}')
        print(df[column].value_counts())

    # Detecting inconsistencies
    print("\nDetecting data type inconsistencies:")
    inconsistent_columns = detect_data_type_inconsistencies(df)

    # Correlation analysis excluding non-numeric columns
    print("\nCorrelation analysis:")
    numeric_df = df.select_dtypes(include=[float, int])
    correlation_matrix = numeric_df.corr()
    print(correlation_matrix)

    # Data profiling report using Sweetviz
    print("\nGenerating Sweetviz report...")
    report = sv.analyze(df, pairwise_analysis="off")
    report.show_html("your_report.html")

    return df

# Usage
csv_path = "data/your_data_file.csv"


df = detect_data_shifts(csv_path)


