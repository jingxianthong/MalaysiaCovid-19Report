import requests
import pandas as pd
import logging
import io

# Set up logging
logging.basicConfig(filename='update.log', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# URL of the CSV file
csv_url = "https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/deaths_malaysia.csv"

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
else:
    logging.error(f"Failed to fetch the CSV file. Status code: {response.status_code}")
