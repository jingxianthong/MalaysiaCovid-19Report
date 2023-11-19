import pandas as pd
import logging

# Configure logging
logging.basicConfig(filename='conversion.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    url = "https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/deaths_malaysia.csv"
    df = pd.read_csv(url)
    html_content = df.to_html()

    with open('output.html', 'w') as file:
        file.write(html_content)

    logging.info("CSV file successfully converted to HTML.")
except Exception as e:
    logging.error(f"An error occurred: {str(e)}")
