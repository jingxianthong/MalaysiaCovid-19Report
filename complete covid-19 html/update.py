import os
import requests
from datetime import datetime

# Directory path to save the file
directory_path = r"C:\Users\thong\OneDrive\Documents\code\malaysia_covid-19 cases\covid-19 html"
file_name = "deaths_malaysia.csv"
file_path = os.path.join(directory_path, file_name)
log_file_path = os.path.join(directory_path, "update.log")

url = "https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/deaths_malaysia.csv"

# Start download timestamp
start_time = datetime.now()
start_time_str = start_time.strftime("%Y-%m-%d %H:%M:%S")

response = requests.get(url)

# End download timestamp
end_time = datetime.now()
end_time_str = end_time.strftime("%Y-%m-%d %H:%M:%S")

with open(log_file_path, "a") as log_file:
    if response.status_code == 200:
        with open(file_path, "wb") as file:
            file.write(response.content)
        log_file.write(f"{start_time_str} - Started downloading '{file_name}' to '{directory_path}'.\n")
        log_file.write(f"{end_time_str} - File '{file_name}' downloaded successfully.\n")
    else:
        log_file.write(f"{end_time_str} - Failed to download the file. Status code: {response.status_code}\n")
