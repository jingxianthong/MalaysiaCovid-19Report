import pandas as pd
import logging

logging.basicConfig(filename='conversion.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    csv_path = "deaths_malaysia.csv"
    df = pd.read_csv(csv_path)
    html_content = df.to_html()

    with open('latest_date.html', 'w') as file:
        file.write(html_content)

    logging.info("CSV file successfully converted to HTML.")
except Exception as e:
    logging.error(f"An error occurred: {str(e)}")
