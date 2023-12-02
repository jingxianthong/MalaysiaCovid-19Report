
## Report: COVID-19 State Data Visualization

### Overview:

The provided code is a Python script for generating HTML files with COVID-19 state data visualizations. The script reads data from a CSV file (`cases_state.csv`) containing COVID-19 cases information for different states. It uses Matplotlib and mpld3 for creating interactive line charts, and the resulting plots are embedded into HTML files.

### Key Components:

1. **`generate_state_html.py`:**
    - Reads COVID-19 cases data from `cases_state.csv`.
    - Takes user input for a specific state.
    - Filters data for the selected state and creates a line chart.
    - Saves the chart as an HTML file with embedded images.

2. **`index.html`:**
    - Main HTML file with links to various data visualizations.
    - Includes links to the Last 7 days, Last 30 days, Full data, and State Graph visualizations.

3. **`state_graph.html`:**
    - HTML file containing links to individual state visualizations.
    - Each state is represented as a hyperlink pointing to its respective HTML file.

4. **State-specific HTML files:**
    - HTML files generated for each state with embedded line charts.
    - Each file is named after the respective state (e.g., `johor.html`, `kedah.html`, etc.).

5. **`verification_results.txt`:**
    - Text file containing verification results.
    - Lists whether each HTML file mentioned in `index.html` and `state_graph.html` exists.

### Execution:

1. **Data Preparation:**
    - COVID-19 cases data is expected to be in the `cases_state.csv` file.

2. **Visualization Generation:**
    - Run `generate_state_html.py`.
    - Input a state name when prompted.
    - Generates state-specific HTML files with embedded charts.

3. **Verification:**
    - Run the verification script to check if HTML files mentioned in `index.html` and `state_graph.html` exist.
    - Results are saved in `verification_results.txt`.

4. **Visualization Access:**
    - Access the visualizations through the links provided in `index.html` and `state_graph.html`.

### Recommendations:

- Ensure that the required libraries (Pandas, Matplotlib, mpld3) are installed.
- Maintain the CSV data file with up-to-date COVID-19 cases information.
- Consider automating the daily update process using a task scheduler.

### Conclusion:

The script facilitates the generation of interactive HTML visualizations for COVID-19 cases data at both the state and national levels. The provided links in `index.html` and `state_graph.html` act as a user-friendly interface for accessing the visualizations.

---

Feel free to modify the report based on your specific requirements or add any additional details.
