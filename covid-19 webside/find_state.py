import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from io import BytesIO
import base64

# CSV_FILE to the CSV file
CSV_FILE = 'cases_state.csv'

# Read the list of states from the text file
with open('states.txt', 'r') as file:
    states = [state.strip().capitalize() for state in file.readlines()]

# Read the CSV data into a pandas DataFrame
df = pd.read_csv(CSV_FILE)

for state_name in states:
    # Filter the data to get only the rows corresponding to state_data
    state_data = df[df['state'].str.strip().str.capitalize() == state_name.strip().capitalize()]

    # Convert the date column to datetime format for better x-axis representation
    state_data.loc[:, 'date'] = pd.to_datetime(state_data['date'])

    # Get the new cases column for state_new_cases
    state_new_cases = state_data['cases_new']

    # Plot the graph
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.plot(state_data['date'], state_new_cases)
    ax.set_xlabel('Date')
    ax.set_ylabel('New Cases')
    ax.set_title(f'Overall count of COVID-19 cases in {state_name}')

    # Set the major locator for years on the x-axis
    years = mdates.YearLocator()
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot as an image in memory
    img_buf = BytesIO()
    fig.savefig(img_buf, format='png')
    img_buf.seek(0)

    # Convert the image to base64 encoding
    img_base64 = base64.b64encode(img_buf.read()).decode()

    # Convert the plot to HTML with embedded image
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Overall count of COVID-19 cases in {state_name}</title>
        <style>
            body {{
                margin: 0;
                padding: 0;
                font-family: 'Arial', sans-serif;
            }}

            img {{
                width: 95%;
                object-fit: contain;
            }}
        </style>
    </head>
    <body>
        <img src="data:image/png;base64,{img_base64}" alt="Overall count of COVID-19 cases in {state_name}">
    </body>
    </html>
    """

    # Save the HTML file with the selected state name
    html_filename = f'{state_name.lower()}.html'
    with open(html_filename, 'w') as file:
        file.write(html_content)
