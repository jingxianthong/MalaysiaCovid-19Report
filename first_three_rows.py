import requests
import pandas as pd
import logging
import io

# Set up logging
logging.basicConfig(filename='update.log', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# path to CSV file
csv_url = "deaths_malaysia.csv"

# Download the CSV file
response = requests.get(csv_url)

# Check if the request was successful
if response.status_code == 200:
    # Decode content to string
    content = response.content.decode('utf-8')
    
    # Read the CSV from the string
    df = pd.read_csv(io.StringIO(content))

    # Extract the latest date
    latest_date = df['date'].max()

    # Log the latest date
    logging.info(f"The latest date in the CSV file is: {latest_date}")

    # Get the first 3 rows of the CSV
    first_3_rows = df.head(3)

    # Log the first 3 rows to date.log
    first_3_rows.to_csv('date.log', index=False)

    # Add the first 3 rows to an HTML file
    first_3_rows.to_html('output.html', index=False)

    logging.info("First 3 rows logged to date.log and added to output.html.")
else:
    logging.error(f"Failed to fetch the CSV file. Status code: {response.status_code}")
