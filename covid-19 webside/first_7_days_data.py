import os
import pandas as pd
from datetime import datetime

# Directory path
directory_path = r"C:\Users\thong\OneDrive\Documents\code\malaysia_covid-19 cases\covid-19 webside"
csv_file_name = "deaths_malaysia.csv"
html_file_name = "first_7_days_data.html"
csv_file_path = os.path.join(directory_path, csv_file_name)
html_file_path = os.path.join(directory_path, html_file_name)

# Read CSV file
df = pd.read_csv(csv_file_path)

# Convert the "date" column to datetime
df['date'] = pd.to_datetime(df['date'])

# Find the latest date in the DataFrame
latest_date = df['date'].max()

# Filter the DataFrame for the first 7 days from the latest date
first_7_days_df = df[df['date'] >= (latest_date - pd.DateOffset(days=6))]

# Convert the filtered DataFrame to HTML
html_content = first_7_days_df.to_html(index=False)

# Write HTML to file
with open(html_file_path, "w", encoding="utf-8") as html_file:
    html_file.write(html_content)

print(f"HTML file '{html_file_name}' has been created in '{directory_path}'.")
