import os
import requests
from datetime import datetime

# Directory path to save the file
directory_path = r"C:\Users\thong\OneDrive\Documents\code\malaysia_covid-19 cases\covid-19 webside"
file_name = "deaths_malaysia.csv"
file_path = os.path.join(directory_path, file_name)
log_file_path = os.path.join(directory_path, "update.log")

url = "https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/deaths_malaysia.csv"
response = requests.get(url)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(log_file_path, "a") as log_file:
    if response.status_code == 200:
        with open(file_path, "wb") as file:
            file.write(response.content)
        log_file.write(f"{timestamp} - File '{file_name}' downloaded successfully to '{directory_path}'.\n")
    else:
        log_file.write(f"{timestamp} - Failed to download the file. Status code: {response.status_code}\n")
