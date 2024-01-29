import pandas as pd
import plotly.express as px

CSV_FILE = 'cases_state.csv'
df = pd.read_csv(CSV_FILE)
df['date'] = pd.to_datetime(df['date'])
unique_years = df['date'].dt.year.unique()
unique_months = df['date'].dt.month.unique()

# Find the current date
current_date = pd.to_datetime('now')

# Calculate the first day of the current month
first_day_current_month = current_date.replace(day=1)

# Find the last month and year in the data
last_month_year = df['date'].max().to_period('M')

# Calculate the last day of the last month
last_day_last_month = (last_month_year.to_timestamp() - pd.DateOffset(days=1)).to_period('D')

# Filter for the last month's data
df_filtered = df[df['date'].dt.to_period('D') >= last_day_last_month]

if not df_filtered.empty:
    fig = px.line(
        df_filtered,
        x='date',
        y='cases_new',
        color='state',
        title=f'COVID-19 Cases in Different States - Last Month ({last_day_last_month.to_timestamp().strftime("%B %Y")})'
    )
    fig.update_layout(xaxis_title='Date', yaxis_title='New Cases')

    # Save the figure as an HTML file
    fig.write_html(f'COVID-19 Cases in Different States Last Month - {last_day_last_month.to_timestamp().strftime("%B %Y")}.html')
else:
    print(f"No data available for the last month ({last_day_last_month.to_timestamp().strftime('%B %Y')}).")
