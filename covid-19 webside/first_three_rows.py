import pandas as pd
import logging
import io
import os

# Set up logging
logging.basicConfig(filename='update.log', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Get the current working directory
current_directory = os.getcwd()

# Path to the local CSV file (assuming deaths_malaysia.csv is in the same directory as the script)
csv_path = os.path.join(current_directory, 'deaths_malaysia.csv')

# Read the CSV file
try:
    with open(csv_path, 'r') as file:
        # Read the CSV from the file
        df = pd.read_csv(file)

        # Extract the latest date
        latest_date = df['date'].max()

        # Log the latest date
        logging.info(f"The latest date in the CSV file is: {latest_date}")

        # Find the first 3 rows of data
        first_3_rows = df.head(3)

        # Log date information from the first 3 rows into date.log
        first_3_dates = first_3_rows['date'].tolist()
        with open('date.log', 'w') as date_file:
            for date in first_3_dates:
                date_file.write(f"{date}\n")

        # Add date information to an HTML file
        html_content = "<html><body><h1>First 3 Dates</h1><ul>"
        for date in first_3_dates:
            html_content += f"<li>{date}</li>"
        html_content += "</ul></body></html>"

        with open('output.html', 'w') as html_file:
            html_file.write(html_content)

except FileNotFoundError:
    logging.error(f"File not found: {csv_path}")
except Exception as e:
    logging.error(f"An error occurred: {str(e)}")
