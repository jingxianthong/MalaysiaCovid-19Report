import os
import pandas as pd
from datetime import datetime

# Directory path
directory_path = r"C:\Users\thong\OneDrive\Documents\code\malaysia_covid-19 cases\covid-19 html"
csv_file_name = "deaths_malaysia.csv"
html_file_name = "deaths_malaysia.html"
csv_file_path = os.path.join(directory_path, csv_file_name)
html_file_path = os.path.join(directory_path, html_file_name)
log_file_path = os.path.join(directory_path, "conversion.log")

try:
    # Read CSV file
    df = pd.read_csv(csv_file_path)

    # Convert DataFrame to HTML
    html_content = df.to_html(index=False)

    # Add stylesheet link
    html_content = f'<head><link rel="stylesheet" href="style.css"></head>{html_content}'

    # Write HTML to file
    with open(html_file_path, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file_path, "a") as log_file:
        log_file.write(f"{timestamp} - CSV file successfully converted to HTML. HTML file saved to '{html_file_path}'.\n")

except Exception as e:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file_path, "a") as log_file:
        log_file.write(f"{timestamp} - An error occurred: {str(e)}\n")
